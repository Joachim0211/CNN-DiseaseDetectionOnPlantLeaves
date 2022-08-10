from unicodedata import name
from flask import Flask, jsonify, request, render_template, redirect, url_for, Response
from flask_dropzone import Dropzone
import numpy as np
from PIL import Image
import PIL
from io import BytesIO
import io
import tensorflow as tf
import os
import cv2 as cv
import base64


basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
predictions = []


app = Flask(__name__)

app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    #Flask-Dropzone config:
    DROPZONE_MAX_FILE_SIZE=1024,  # set max size limit to a large number, here is 1024 B
    DROPZONE_TIMEOUT=5 * 60 * 1000  # set upload timeout to a large number, here is 5 minutes
)

dropzone = Dropzone(app)
MODEL = tf.keras.models.load_model("./models/3")
class_names = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']
global submission
submission = 'Your file name'
#global result

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('file').read()
    npimg = np.fromstring(f, np.uint8)
    #f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    print(f)
    img = cv.imdecode(npimg,cv.IMREAD_COLOR)
    img_0 = cv.resize(img,(256,256))
    img_1 = np.array(img_0)
    img_ready = np.expand_dims(img_1, 0) 
    
    predictions = MODEL.predict(img_ready)
    score = tf.nn.softmax(predictions[0])
    
   
    # global result1
    # if 'Early' in a.filename:
    #     result1 = 'Early Blight'
    # elif 'RS_LB' in a.filename:
    #     result1 = 'Late Blight'
    # elif 'RS_HL' in a.filename:
    #     result1 = 'Your picture was labeled "Healthy"'
    # else:
    #     result1 = a.filename
        
    if 100 - np.max(score) < 60:
        result = "The analysis shows no clear result"
    else:
        if class_names[np.argmax(score)] == 'Potato___healthy':
            result = "Your plant is healthy with a {:.2f} percent confidence.".format(100 - np.max(score))
            result1=0
        elif class_names[np.argmax(score)] == 'Potato___Early_blight':
            result = "Your plant shows symptoms of {} with a {:.2f} percent confidence.".format(class_names[np.argmax(score)], 100 - np.max(score))
            result1=1
        elif class_names[np.argmax(score)] == 'Potato___Late_blight':
            result = "Your plant shows symptoms of {} with a {:.2f} percent probability.".format(class_names[np.argmax(score)], 100 - np.max(score))
            result1=2
    
    print('app run')


    return jsonify(data=result, errors=result1)



@app.route('/')
def show():    
    return render_template('index.html')


@app.route('/answer')
def up():
    return "Your picture is a tiger"  #render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)