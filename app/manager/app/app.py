#!/usr/bin/python3.8

from flask import Flask, request, jsonify   # flask for the server
from multiprocessing import Lock            # Lock for concurrent requests
import time                                 # HACK time.sleep for testing concurrency
import container
import os

# Locks
test_lock = Lock()
app = Flask(__name__)

container = container.Container()

@app.route('/version', methods=['POST'])
def use():
    """
    Change the tag of the image used by this device
    """
    content = request.json
    new_tag = content['tag']
    container.switch_version(new_tag)
    return jsonify({"success" : True})

@app.route('/version', methods=['GET'])
def version():
    """
    Get the version (tag) used by this device
    """
    v = container.version()
    return jsonify({ "version" : v })

@app.route('/status')
def status():
    stat = container.status()
    return jsonify({
        'status' : str(stat)
    })

if __name__ == '__main__':
    app.run()