from flask import Flask, render_template, request, redirect, url_for
# from flask_uploads import UploadSet, configure_uploads, IMAGES
import os
import pymongo	
import datetime

app = Flask(__name__)
	
MONGO_URI = os.getenv('MONGO_URI')
DATABASE_NAME = 'cars_listing'
COLLECTION_NAME = 'car_plate'
COLLECTION_REF = 'car_menu'

# upload_dir = "/static/uploads/images/"
# TOP_LEVEL_DIR = os.path.abspath(os.curdir)
# app.config['UPLOADED_IMAGES_DEST'] = TOP_LEVEL_DIR + upload_dir
# app.config['UPLOADS_DEFAULT_DEST'] = 

# STEP 0 - Create the connection to mongo
# 0.1. Retrieve the environment variables
# def mongo_connect(url):
#     try:
#         conn = pymongo.MongoClient(MONGO_URI)
#         print("Mongo is connected")
#         return conn
#     except pymongo.errors.ConnectionFailure as e:
#         print("Could not connect to MongoDB: %s") % e

# 0.2. Create the connection
conn = pymongo.MongoClient(MONGO_URI)
datalink = conn[DATABASE_NAME][COLLECTION_NAME]
data_ref = conn[DATABASE_NAME][COLLECTION_REF]

# STEP 1 - Create a home route and test it
@app.route('/') # map the root route to the index function
def index():
    results = datalink.find({})
    # for i in results:
    #     results[i].car_specs.reg_date = datetime.datetime.strftime(results[i].car_specs.reg_date, '%d.%m.%Y')
    return render_template ("index.html", detail=results)
    

@app.route('/vehicle/add')
def add_listing():
    results = data_ref.find({})
    return render_template('add_listing.html', detail=results) 
    
@app.route('/vehicle/add_process')
def insert_listing():
    return render_template('index.html')

@app.route('/vehicle/edit')
def edit_listing():
    return render_template('edit_listing.html')

@app.route('/vehicle/delete')
def delete_listing():
    return render_template('delete_listing.html')




# "magic code" -- boilerplate
if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)