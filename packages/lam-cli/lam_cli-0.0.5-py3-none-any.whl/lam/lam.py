#!/usr/bin/env python3

import json
import logging
import os
import shutil
import socket
import subprocess
from datetime import datetime

import click

jq_path = 'jq'

def generate_distinct_id(workspace_id, flow_id):
    user_id = os.getuid()
    hostname = socket.gethostname()
    return f"{user_id}_{hostname}_{workspace_id}_{flow_id}"

def track_event(event_name, properties, workspace_id="local", flow_id="local"):
    logging.info(f"Event {event_name} triggered, with properties: {properties}")

def parse_program(program):
    logging.info(f"Parsing program: {program}")

    split_by_lines = program.split('\n')
    return ''.join(line for line in split_by_lines if line and not line.strip().startswith('#'))

def run_jq(jq_script, input_data):
    logging.info(f"Running jq script {jq_script} with input data {input_data}")
    process = subprocess.Popen([jq_path, '-c', jq_script], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = process.communicate(input=input_data)
    if error:
        logging.error(f"Error running jq: {error}")
    return output, error

def process_input(input_json, workspace_id, flow_id):
    logging.info(f"Processing input_json: {input_json}")
    try:
        json.loads(input_json)
        return input_json, None
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON input: {e}")
        track_event('lam.run.error', {'error': f"Invalid JSON input: {e}", 'workspace_id': workspace_id, 'flow_id': flow_id}, workspace_id, flow_id)
        return None, str(e)

def handle_jq_output(output, as_json, workspace_id, flow_id):
    logging.info(f"Handling jq output: {output}")
    try:
        json_output = json.loads(output)
        # Make sure the output has a top-level object
        if not isinstance(json_output, dict):
            track_event('lam.run.warn', {'error': 'Invalid JSON output', 'workspace_id': workspace_id, 'flow_id': flow_id}, workspace_id, flow_id)
            return {"lam.result": json_output} if as_json else output, None
        return json_output if as_json else output, None
    except json.JSONDecodeError as e:
        logging.error("Failed to parse JSON output, may be multiple JSON objects. Attempting to parse as JSON lines.")
        track_event('lam.run.warn', {'error': f"Invalid JSON output: {e}", 'workspace_id': workspace_id, 'flow_id': flow_id}, workspace_id, flow_id)
        if as_json:
            json_objects = [json.loads(line) for line in output.strip().split('\n') if line]
            return {"lam.concatenated": json_objects}, None
        return output, "Failed to parse JSON output."

def write_to_result_file(result, result_file):
    with open(result_file, 'w') as file:
        file.write(json.dumps(result, indent=4))

@click.group()
def lam():
    pass

@lam.command()
@click.argument('program', type=str)
@click.argument('input_json', type=str)
@click.option('--workspace_id', default="local", help="Workspace ID")
@click.option('--flow_id', default="local", help="Flow ID")
@click.option('--as-json', is_flag=True, default=True, help="Output as JSON")
def run(program, input_json, workspace_id, flow_id, as_json):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file = f"lam_run_{workspace_id}_{flow_id}_{timestamp}.log"
    result_file = f"lam_result_{workspace_id}_{flow_id}_{timestamp}.json"

    # Now configure logging with the determined log file name
    logging.basicConfig(level=logging.INFO, filename=log_file, filemode='w',
                        format='%(asctime)s - %(levelname)s - %(message)s')

    logging.info(f"Logging to {log_file}")
    logging.info(f"Running command with program: {program}, input_json: {input_json}, workspace_id: {workspace_id}, flow_id: {flow_id}, as_json: {as_json}")
    if not shutil.which("jq"):
        logging.error("Unable to find jq, killing process")
        click.echo({"lam.error": "jq is not installed"}, err=True)
        track_event('lam.run.error', {'error': 'jq is not installed', 'workspace_id': workspace_id, 'flow_id': flow_id}, workspace_id, flow_id)
        write_to_result_file({"lam.error": "jq is not installed"}, result_file) 
        return

    input_data, error = process_input(input_json, workspace_id, flow_id)
    if error:
        click.echo({"lam.error": f"Invalid input: {error}"}, err=True)
        track_event('lam.run.error', {'error': f"Invalid input: {error}", 'workspace_id': workspace_id, 'flow_id': flow_id}, workspace_id, flow_id)
        write_to_result_file({"lam.error": f"Invalid input: {error}"}, result_file)
        return

    jq_script = parse_program(program)
    track_event('lam.run.start', {'script': jq_script, 'as_json': as_json, 'workspace_id': workspace_id, 'flow_id': flow_id}, workspace_id, flow_id)
    output, jq_error = run_jq(jq_script, input_data)

    if jq_error:
        click.echo({"lam.error": jq_error}, err=True)
        track_event('lam.run.run_jq_error', {'error': jq_error, 'workspace_id': workspace_id, 'flow_id': flow_id}, workspace_id, flow_id)
        write_to_result_file({"lam.error": jq_error}, result_file)
        return

    result, error = handle_jq_output(output, as_json, workspace_id, flow_id)
    if error:
        click.echo({"lam.error": error}, err=True)
        track_event('lam.run.handle_jq_output_error', {'error': error, 'workspace_id': workspace_id, 'flow_id': flow_id}, workspace_id, flow_id)
        write_to_result_file({"lam.error": error}, result_file)
    else:
        click.echo(json.dumps(result, indent=4) if as_json else result)
        track_event('lam.run.success', {'workspace_id': workspace_id, 'flow_id': flow_id}, workspace_id, flow_id)
        write_to_result_file(result, result_file)

    logging.info("Run complete, waiting for event logger to finish")

if __name__ == '__main__':
    lam()
