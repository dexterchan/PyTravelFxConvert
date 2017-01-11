import os
import sys
from flask import abort
from flask import jsonify
import json
from flask import Flask, request, redirect, send_from_directory,Response
from werkzeug import secure_filename
import logging

# Initialize the Flask application
app = Flask(__name__, static_url_path='/static')



@app.route('/allccyset')
def allccyset():
    ccyList=["AUD","CAD","CHF","CNY","EUR","GBP","HKD","INR","JPY","KRW","MYR","NZD","SGD","THB","TWD","USD"]
    #resp = Response(response=ccyList,status=200, mimetype="application/json")
    #return jsonify(ccyList)
    return Response(json.dumps(ccyList),  mimetype='application/json')

@app.route('/')
def home():
    return  send_from_directory('static/', 'indexFx.html')



@app.route('/js/<path:path>')
def send_js(path):
    print ('get js')
    return send_from_directory('static/js', path)

if __name__ == '__main__':
    app.run(
        host= '0.0.0.0',
        port=int("8080"),
        debug=True
    )
