import logging
import os
import zlib
from PIL import Image, ImageOps
from io import BytesIO,StringIO
from flask import Flask, request
from github_api import *
import glob

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
    stream = BytesIO(content)

    image = Image.open(dict(request.files)['filename'])
    image = ImageOps.exif_transpose(image)
    put_file(filename, content)
    fp = BytesIO()
    
    
    image.save("static/"+filename, filename.split('.')[1],optimize = True,quality=75)
    put_file("c_" + filename, fp.getvalue())
    
    fp.close()
    stream.close()
    return "Ok"


if __name__ == '__main__':
    app.run(debug=True, port=5555, host='0.0.0.0')
