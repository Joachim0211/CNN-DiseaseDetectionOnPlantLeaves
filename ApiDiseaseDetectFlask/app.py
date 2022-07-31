from unicodedata import name
from flask import Flask, jsonify, request, render_template
from flask_dropzone import Dropzone
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    # Flask-Dropzone config:
    DROPZONE_MAX_FILE_SIZE=1024,  # set max size limit to a large number, here is 1024 MB
    DROPZONE_TIMEOUT=5 * 60 * 1000  # set upload timeout to a large number, here is 5 minutes
)

dropzone = Dropzone(app)


stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]

@app.route('/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    return render_template('index.html')



@app.route('/store', methods = ['POST']) # the browser send a message to make a store (request)
def create_store():
    request_data = request.get_json()
    new_store = {
            'name': request_data['name'],
            'items': []
            }
    stores.append(new_store)
    return jsonify(new_store) #this needs to be jsonified since we must! return a string

@app.route('/store/<string:name>') #the browser sends a get message
def get_store(name):
    #iterate over store
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

@app.route('/store')
def get_stores():
    return jsonify({'stores': stores}) #json takes only dic, so the stores-list must be converted to a dic

@app.route('/store/<string:name>/item',  methods = ['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(store)
    return jsonify({'message': 'store not found'})

@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'item not found'})

if __name__ == "__main__":
    app.run(debug=True)

app.run(port = 5000)