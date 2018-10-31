from flask import Flask, request
import os
from flask import jsonify
import sys
from io import BytesIO
from flask import send_file
import numpy as np
import cv2

basedir = os.path.abspath(os.path.dirname(__file__))

# create the application object
app = Flask(__name__)

def load_image_into_numpy_array(image):
  (im_width, im_height) = image.size
  return np.array(image.getdata()).reshape(
      (im_height, im_width, 3)).astype(np.uint8)

@app.route('/uploadimage', methods=['POST'], strict_slashes=False)
def api_upload():
    file_dir = basedir + 'photo'
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)] = requesrint(r.data)
    nparr = np.fromstring(r.data, np.uint8)
    print(nparr)
    img = cv2.imdede(nparr, cv2.IMREAD_COLOR)
    print(img)
    cv2.imshow("image", img)

    return jsonify({"errno":0, "msg":"succeed ","token":1})

if __name__ == "__main__":
    print(basedir)
    app.run(host='0.0.0.0', debug=True)