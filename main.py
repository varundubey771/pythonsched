# -*- coding: utf-8 -*-
import logging
from flask import Flask, request


# Load data from config.ini file
# config = configparser.ConfigParser()
# config.read('config.ini')


# Initial Flask app
app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name  



if __name__ == "__main__":
    # Running server
    app.run(debug=True)
