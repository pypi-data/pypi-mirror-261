from typing import Dict, Any, Tuple
from flask import Flask, request, jsonify
from waitress import serve
import logging
import sys
import os
import json

from .activity_logger import ActivityLogHandler
from .const import *

FUNCTION_NAME=os.environ.get('FUNCTION_NAME', 'default-function-name')
LOG_LEVEL=os.environ.get('LOG_LEVEL', 'INFO')
LOG_BUFFER_CAPACITY=int(os.environ.get('LOG_BUFFER_CAPACITY', "1000"))
LOG_BUFFER_FLUSH_LEVEL=int(os.environ.get('LOG_BUFFER_FLUSH_LEVEL', "10"))

_logger = logging.Logger(FUNCTION_NAME)
_handler = logging.StreamHandler(stream=sys.stdout)
_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
_handler.setFormatter(_formatter)
_logger.addHandler(_handler)
_handler.setLevel(LOG_LEVEL)

def _log(f):
    def wrap(*args, **kwargs):
        logger = logging.Logger(__name__)

        engineEndpoint= request.headers.get(EngineAPIEndpointHeader, type=str),
        fileUploadPath= request.headers.get(ActivityFileUploadHeader, type=str),

        token = request.headers.get(WorkflowTokenHeader)

        endpoint = engineEndpoint + fileUploadPath
        handler = ActivityLogHandler(endpoint=endpoint, token=token, capacity=LOG_BUFFER_CAPACITY, flushLevel=LOG_BUFFER_FLUSH_LEVEL)
        logger.setLevel(LOG_LEVEL)
        logger.info(f"calling function: {FUNCTION_NAME}")
        logger.addHandler(handler)

        return f(logger=logger, *args, **kwargs)
    return wrap


def call_ready():
    return jsonify({ "status": "ready" }), 200

def call(handler):
    return lambda: handle(handler)

@_log
def handle(handler, logger=None) -> Tuple[Dict[str, Any], int]:
    resp, status_code = None, 0
    try:
        req = json.loads(request.data)
        if req is None:
            req = {}
        req["metadata"] = {
            "activityID": request.headers.get(ActivityIDHeader),
            "environmentID": request.headers.get(EnvironmentIDHeader),
            "environmentName": request.headers.get(EnvironmentNameHeader),
        }  
        resp = handler(logger, req)
        resp, status_code = jsonify(resp), 200        
    except Exception as e:
        resp, status_code = jsonify({ "error": str(e) }), 500
    return resp, status_code


def serve_function(handler, host='0.0.0.0', port=5000):
    _logger.info(f'Starting Python Function {FUNCTION_NAME} ...')

    app = Flask(FUNCTION_NAME)

    app.add_url_rule('/_/ready', methods=['GET'], view_func=call_ready)
    app.add_url_rule('/', methods=['POST'], view_func=call(handler))

    serve(app, host=host, port=port)
