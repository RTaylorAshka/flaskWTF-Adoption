from flask import Flask, request, render_template, redirect, flash, session

from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db, Pet
from forms import NewPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///AdoptionDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'oooitsasecret'

app.app_context().push()
connect_db(app)
db.create_all()

# Get homepage template, pass all pets in database.
@app.route('/')
def get_homepage():

    pets = Pet.query.all()
    return render_template('home.html', pets = pets)

# Make form for new pet and pass to template. If valid form, add pet to database.
@app.route('/add', methods = ['GET', 'POST'])
def get_pet_form():
    form = NewPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name = name, species = species, photo_url = photo_url, age = age, notes = notes)
        db.session.add(pet)
        db.session.commit()

        return redirect('/')
    
    else:
        return render_template('pet-form.html', form = form)
    

# Get template displaying pet info and edit form. If valid form, update pet in database.
@app.route('/<int:pet_id>', methods = ['GET', 'POST'])
def get_pet_page(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm()

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.available = form.available.data
        pet.notes = form.notes.data

        db.session.commit()

        return redirect('/')

    else:

        form.photo_url.data = pet.photo_url
        form.available.data = pet.available
        form.notes.data = pet.notes

        return render_template('pet-page.html', pet = pet, form = form)



    

        