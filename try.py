from unicodedata import name
# from flask import Flask, jsonify, request, render_template, redirect, url_for, Response
# from flask_dropzone import Dropzone
import numpy as np
from PIL import Image
import PIL
from io import BytesIO
import io
#import tensorflow as tf
import os
import time


# MODEL = tf.keras.models.load_model("./models/3")
class_names = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']

def something():
    f = PIL.Image.open('./FM_DerTiger.jpg')
    print(type(f))
    img_0 = f.resize((256,256),  Image.Resampling.LANCZOS)
    img_1 = np.array(img_0)
    print(img_1.shape)
    img_2 = np.expand_dims(img_1, 0)
    print(img_2.shape)



    
    #print(img_3.shape)

    # #img_array = tf.keras.utils.img_to_array(img)

    # # img_batch = tf.expand_dims(img_array, 0)

    # predictions = MODEL.predict(img_batch)
    # score = tf.nn.softmax(predictions[0])
    
    

    # global result1
    # if 'Early' in f.filename:
    #     result1 = 'Early Blight'
    # elif 'RS_LB' in f.filename:
    #     result1 = 'Late Blight'
    # elif 'RS_HL' in f.filename:
    #     result1 = 'Your picture was labeled "Healthy"'
    # else:
    #     result1 = f.filename
    #f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    
    # img = tf.image.resize(f, [256, 256])
    # # img_array = tf.keras.utils.img_to_array(img)
    # # img_batch = tf.expand_dims(img_array, 0)
    # # img.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    # img_1 = np.array(PIL.Image.open(img))
    # img_batch = np.expand_dims(img_1, 0)      
    #img = tf.image.resize(f, [256, 256])
    
    # if 100 - np.max(score) < 60:
    #     result = "The analysis shows no clear result"
    # else:
    #     if class_names[np.argmax(score)] == 'Potato___healthy':
    #         result = "Your plant is healthy with a {:.2f} percent confidence.".format(100 - np.max(score))
    #     elif class_names[np.argmax(score)] == 'Potato___Early_blight':
    #         result = "Your plant shows symptoms of {} with a {:.2f} percent confidence.".format(class_names[np.argmax(score)], 100 - np.max(score))
    #     elif class_names[np.argmax(score)] == 'Potato___Late_blight':
    #         result = "Your plant shows symptoms of {} with a {:.2f} percent confidence.".format(class_names[np.argmax(score)], 100 - np.max(score))
    
    # time.sleep(3)
    print('woken up')
    result = ''
    result1 = ''

    return result, result1

something()
