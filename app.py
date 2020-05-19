from flask_debugtoolbar import DebugToolbarExtension
from flask import Flask, request, redirect, render_template, flash
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
# run this line of code on the command line to create the table only once
# db.create_all()
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def home_page():
    """Shows homepage listing pets"""
    pets = Pet.query.all()

    return render_template("homepage.html", pets=pets)



@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form."""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url .data
        age = form.age.data
        notes = form.notes.data
        flash(f"Added {name}")
        return redirect("/")
    else:
        return render_template("add_pet.html", form=form)




