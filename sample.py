import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import json
import flask
from flask import (
    Response,
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

def run() :
    # Load the diabetes dataset
    diabetes = datasets.load_diabetes()

    # Use only one feature
    diabetes_X = diabetes.data[:, np.newaxis, 2]

    # Split the data into training/testing sets
    diabetes_X_train = diabetes_X[:-20]
    diabetes_X_test = diabetes_X[-20:]

    # Split the targets into training/testing sets
    diabetes_y_train = diabetes.target[:-20]
    diabetes_y_test = diabetes.target[-20:]

    # Create linear regression object
    regr = linear_model.LinearRegression()

    # Train the model using the training sets
    regr.fit(diabetes_X_train, diabetes_y_train)

    # Make predictions using the testing set
    diabetes_y_pred = regr.predict(diabetes_X_test)

    # Return test and predictions.
    json_dict = {}
    X_list = []
    Xs = diabetes_X_test.tolist()

    for X in Xs:
        X_list.append(X[0])

    json_dict['diabetes_X_test'] = X_list
    json_dict['diabetes_y_test'] = diabetes_y_test.tolist()
    json_dict['diabetes_y_pred'] = diabetes_y_pred.tolist()
    print(json_dict)

    json_object = jsonify(json_dict)
    print("jsonify Okay")

    response = json_object
    response.headers['Content-Type'] = "application/json"

    print(response)

    return(response)
