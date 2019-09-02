coll.find({'car_tag.availability':'Available'}).pretty()

coll.find({
    'car_tag.availability':'Sold','car_tag.car_make':'Volvo'
})

