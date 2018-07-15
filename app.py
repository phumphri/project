

from requests.models import Response
import pandas as pd
import numpy as np
import math
import socket
import os
from os import environ
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
    # print(request.headers)
    return render_template("index.html")

# I'm kicking around the idea of having boostrap version for phones, tables, laptops as well as large screens.
# @app.route("/phones")
# def phones():
#     # print(request.headers)
#     return render_template("phones.html")


# Copy this and point the endpoint to your API.
@app.route('/api/sample', methods=['GET'])
def api_sample():

    if request.method == 'GET':

        return sample.run()


if __name__ == "__main__":
    hostname = socket.gethostname()
    print("socket.hostname():", hostname)

    if (hostname == 'XPS'):
        # Patrick's workstation
        # app.run(debug=True)
        print("Port", environ.get("PORT", "Not Found"))
        app.run(debug=False, host='0.0.0.0', port=5000)

    elif (hostname == 'DESKTOP-S08TN4O'):
        # Patrick's Laptop
        app.run(debug=True)
    else:
        # Heroku
        print("Port", environ.get("PORT", "Not Found"))
        app.run(debug=False, host='0.0.0.0',
                port=int(environ.get("PORT", 5000)))
