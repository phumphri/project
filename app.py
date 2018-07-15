

from requests.models import Response
import pandas as pd
import numpy as np
import math
import socket
import os
import json
import flask
from flask import (
    Response,
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from flask_cors import CORS
import os.path


# Assigning the Flask framework.
app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    print(request.headers)
    return render_template("index.html")

@app.route('/sample', methods=['GET'])
def sample():

    if request.method == 'GET':

        try:
            # Create json dictionary to hold the data.
            json_dict = {}
            json_dict['Sample'] = "sample"

            json_object = jsonify(json_dict)
            print("jsonify Okay")

            response = json_object
            response.headers['Content-Type'] = "application/json"

            return response

        except Exception as e:
            print('/sample failed', str(e))
            return str(e)

if __name__ == "__main__":
    hostname = socket.gethostname()
    print("socket.hostname():", hostname)
    
    if (hostname == 'XPS'):
        app.run(debug=True)
    elif (hostname == 'DESKTOP-S08TN4O'):  
        app.run(debug=True)
    else:
        from os import environ
        print("Port", environ.get("PORT", "Not Found"))
        app.run(debug=False, host='0.0.0.0', port=int(environ.get("PORT", 5000)))

