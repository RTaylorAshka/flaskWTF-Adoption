from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

# Connects database to flask app
def connect_db(app):
    
    
    db.app = app
    db.init_app(app)


# Pet model for database.
class Pet(db.Model):

    __tablename__ = 'pets'


    id = db.Column(db.Integer,
                    primary_key = True,
                    autoincrement = True
    )
    name = db.Column(db.String,
                      nullable = False
                      )
    species = db.Column(db.String,
                        nullable = False
                        )
    photo_url = db.Column(db.String,
                           default = 'http://clipart-library.com/images/rTLo9BGkc.png'
                           )
    age = db.Column(db.Integer)

    notes = db.Column(db.String)

    available = db.Column(db.Boolean,
                           default = True
                           )