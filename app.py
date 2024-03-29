#!/usr/bin/env python

from config import Config
from flask_bootstrap import Bootstrap
from flask_sslify import SSLify
from flask import Flask, render_template, request, jsonify
import atexit, os, os.path, json

# Init Flask WebApp
app = Flask(__name__)

# Setup the Config.py file
app.config.from_object(Config)

# Configure the Flask App to use Bootstrap
bootstrap = Bootstrap(app)

# Configure SSL connection with SSLify
sslify = SSLify(app)

# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
# port = int(os.getenv('VCAP_APP_PORT', 8000))
port = int(os.getenv('PORT', 8000))

@app.route('/')
def root():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
