import logging
import os

from flask import Flask, request

from github_api import *

try:
    app = Flask(__name__)

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('werkzeug').setLevel(logging.ERROR)
except Exception as e:
    logging.exception("Error at startup")

@app.route('/ping')
def ping():
    logging.info('/ping')
    return "ping Ok"


@app.route('/check')
def check():
    logging.info('/check')

    
    filename = request.args.get('filename')
    ret = check_file_exist(filename)

    return str(ret)


@app.route('/get')
def get():
    logging.info('/get')

   
    filename = request.args.get('filename')
    file = get_file(filename)
 
    return file


@app.route('/put', methods=['POST'])
def put():
    content = dict(request.files)['filename'].read()
    filename = dict(request.files)['filename'].filename
   
    put_file(filename, content)
    return "Ok"


if __name__ == '__main__':
    app.run(debug=True, port=5555, host='0.0.0.0')
