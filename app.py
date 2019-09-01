from flask import Flask, render_template, request, redirect, url_for
# from flask_uploads import UploadSet, configure_uploads, IMAGES
import os
import pymongo	
import datetime
from bson.objectid import ObjectId

app = Flask(__name__)
	
MONGO_URI = os.getenv('MONGO_URI')
DATABASE_NAME = 'cars_listing'
COLLECTION_NAME = 'car_plate'

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

# STEP 1 - Create a home route and test it
@app.route('/') # map the root route to the index function
def index():
    results = datalink.find({})
    return render_template ("index.html", detail=results)
@app.route('/', methods=["POST"])
def search():
#     # Getting the data from the form
    car_make = request.form.get('search-car-make')
    car_type = request.form.get('search-car-type')
    year_of_make = int(request.form.get('search-year-of-make'))
    availability = request.form.get('availability')
    
    if car_make == 'all' and car_type == 'all' and year_of_make == 0 and availability == 'all' :
        result = datalink.find({})
        return render_template("index.html", detail=result)
  
    elif car_make != 'all':     
        result = datalink.find({
            'car_tag.car_make' : car_make
        })
        return render_template("index.html", detail=result)
    
    elif car_type != 'all':     
        result = datalink.find({
            'car_tag.car_type' : car_type
        })
        return render_template("index.html", detail=result)

    elif year_of_make > 0:     
        result = datalink.find({
            'car_tag.year_of_make': year_of_make
        })
        return render_template("index.html", detail=result)
    
    elif availability != 'all':     
        result = datalink.find({
            'car_tag.availability' : availability
        })
        return render_template("index.html", detail=result)
    
    
    # if year_of_make == 0:
    #     result = datalink.find({})
    #     return render_template("index.html", detail=result)
    # else:
    #     result = datalink.find({
    # # #         'car_tag.availability': availability,
    #         'car_tag.year_of_make': year_of_make
    #     })
    #     return render_template("index.html", detail=result)


@app.route('/vehicle/add')
def add_listing():
    return render_template('add_listing.html', data={}) 
    
@app.route('/vehicle/add', methods=["POST"])
def insert_listing():
    # Getting the data from the form
    car_make = request.form.get('car-make')
    car_model = request.form.get('car-model')
    reg_year = int(request.form.get('year'))
    car_price = int(request.form.get('car-price'))
    mileage = int(request.form.get('mileage'))
    description = request.form.get('description')
    car_type = request.form.get('car-type')
    availability = request.form.get('availability')

    datalink.insert({
        'car_tag' : {
            'car_make' : car_make, # right hand side title is not in quotes, so it's a variable
            'car_model': car_model,
            'year_of_make':reg_year,
            'car_type': car_type,
            'availability':availability
        },
        'car_price' : car_price,
        'mileage': mileage,
        'description': description
    })
    
    return redirect(url_for('index'))
    
@app.route('/vehicle/<taskid>/edit')
def edit_listing(taskid):
    vehicle = datalink.find_one({
        "_id":ObjectId(taskid)
    })
    return render_template('edit_listing.html', v=vehicle)

@app.route('/vehicle/<taskid>/edit', methods=["POST"])
def update_listing(taskid):
    # Getting the data from the form
    car_make = request.form.get('car-make')
    car_model = request.form.get('car-model')
    reg_year = int(request.form.get('year'))
    car_price = int(request.form.get('car-price'))
    mileage = int(request.form.get('mileage'))
    description = request.form.get('description')
    car_type = request.form.get('car-type')
    availability = request.form.get('availability')
    
    datalink.update({
        '_id':ObjectId(taskid)
    }, {
        '$set': {
        'car_tag' : {
            'car_make' : car_make, # right hand side title is not in quotes, so it's a variable
            'car_model': car_model,
            'year_of_make':reg_year,
            'car_type': car_type,
            'availability':availability
        },
        'car_price' : car_price,
        'mileage': mileage,
        'description': description
        }
    })    
    return redirect(url_for('index'))

@app.route('/vehicle/<taskid>/confirm_delete')
def delete_listing(taskid):
    task = datalink.find_one({
        '_id':ObjectId(taskid)
    })
    return render_template('delete_listing.html',taskid=task)
    
@app.route('/vehicle/<taskid>/delete')
def delete(taskid):
    datalink.delete_one({
        '_id':ObjectId(taskid)
    })
    return redirect(url_for('index'))



# @app.route('/vehicle/search_listing', methods=["POST"])
# def search_listing():
#     # car_make = request.form.get('search-car-make')
#     # car_model = request.form.get('car-model')
#     # reg_year = int(request.form.get('search-year-of-make'))
#     # car_price = int(request.form.get('search-price-max'))
#     availability = request.form.get('availability')

#     if (availability == 'available'):
#         result = datalink.coll.find({'car_tag.availability':'Available'})
#     return render_template('search_listing.html')
    
    


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)