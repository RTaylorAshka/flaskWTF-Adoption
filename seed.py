from models import db, Pet
from app import app
import random


db.drop_all()
db.create_all()

animals = [
    ['Max','Dog','https://th.bing.com/th/id/OIF.xk5rU2kRvA1hqsxuzDc8bQ?pid=ImgDet&rs=1'],
    ['Luna','Cat','https://i.pinimg.com/474x/8c/66/13/8c6613045cb22eb4e3b8b7cab8141033.jpg'],
    ['Rocky','Porcupine','https://i.pinimg.com/originals/e7/6d/c8/e76dc8a1af8da659d4f801cab35200e0.jpg'],
    ['Gizmo','Dog','https://external-preview.redd.it/JY_JxohnIcjJZL1L6TgvcQXYfk-DZEe1tgRT2itJpXI.jpg?auto=webp&s=500a5aecd349afa24fe7763e5ce3cf2742796561'],
    ['Cleo','Cat','https://katwerx.com/wp-content/uploads/2021/07/Rosario-scaled.jpg'],
    ['Zeus','Porcupine','https://fox4kc.com/wp-content/uploads/sites/16/2014/09/20140919_171847.jpg?w=900'],
    ['Mango','Dog','https://preview.redd.it/bbdclcc7wua21.jpg?auto=webp&s=7da32706b404f5defab76f98c6596b0841e6a527'],
    ['Sparky','Cat','https://cache.desktopnexus.com/thumbseg/1355/1355594-bigthumbnail.jpg']
    
]

for a in animals:
    new_pet = Pet(name = a[0], species = a[1], photo_url = a[2])
    db.session.add(new_pet)

db.session.commit()