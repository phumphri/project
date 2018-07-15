

from requests.models import Response
import pandas as pd
import numpy as np
import math
import socket
import os
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
import sample



# Assigning the Flask framework.
app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    print(request.headers)
    return render_template("index.html")


@app.route('/api/sample', methods=['GET'])
def api_sample():

    if request.method == 'GET':

        return sample.run()


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
        app.run(debug=False, host='0.0.0.0',
                port=int(environ.get("PORT", 5000)))
