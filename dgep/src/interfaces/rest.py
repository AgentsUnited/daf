from flask import Flask, request, g, Response
from flask_restful import Resource, Api
import json
from flask_jsonpify import jsonify
from dgep_interface import DGEPInterface
from gevent import pywsgi
import dgep_endpoint

""" Provides a RESTful endpoint for DGEP using Flask
"""

''' Mapping of URL components to parameters expected by DGEP
    This allows URLs in the form /<command>/<parameter>/... but isn't
    essential: the parameters can still be passed in a JSON object in a POST
    request. Also, not all parameters are required - required parameters are
    enforced by the DGEP endpoint definition'''
parameters = {
    "protocol": ["name", "action"], # corresponds to /protocol/<name>/<action>
    "join": ["dialogueID"], #correspnds to /join/<dialogueID>
    "moves": ["dialogueID"], # and so on...
    "new": ["protocol"],
    "plugin": ["name", "action"]
}

app = Flask(__name__)

@app.route('/<method>',methods=['GET', 'POST'])
def dgep_route_with_no_params(method):
    data = {}

    if request.method == "POST":
        data = request.get_json()

    r = dgep_endpoint.invoke(Rest.dgep, method, data)
    print("Sending response")
    print(r)
    return jsonify(r)

@app.route('/<method>/<parameter>', methods=['GET', 'POST'])
def dgep_route_with_one_param(method, parameter):
    data = {}

    if request.method == "POST":
        data = request.get_json()

    if method in parameters.keys():
        data[parameters[method][0]] = parameter

    return jsonify(dgep_endpoint.invoke(Rest.dgep, method, data))

@app.route('/<method>/<parameter_one>/<parameter_two>', methods=['GET', 'POST'])
def dgep_route_with_two_params(method, parameter_one, parameter_two):
    data = {}

    if request.method == "POST":
        data = request.get_json()

    if method in parameters.keys():
        data[parameters[method][0]] = parameter_one
        data[parameters[method][1]] = parameter_two

    return jsonify(dgep_endpoint.invoke(Rest.dgep, method, data))

class Rest(DGEPInterface):
    """ Wrapper class for the RESTful interface
    """

    dgep = None

    def run(self, dgep):
        Rest.dgep = dgep
        http_server = pywsgi.WSGIServer(('', 8888), app)
        http_server.serve_forever()
