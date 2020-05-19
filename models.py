from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
DEFAULT_IMAGE_URL = 'https://images.unsplash.com/photo-1565945887714-d5139f4eb0ce?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60'

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)


class Pet(db.Model):

    """Models for pet adoption """
    __tablename__ = 'pets'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    species = db.Column(db.Text, nullable=False, unique=False)
    photo_url = db.Column(db.Text, default=DEFAULT_IMAGE_URL)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, unique=False, default=True)


    def __repr__(self):
        """Show info about pet"""

        p = self
        return f"<Pet {p.id} {p.name } {p.species} {p.photo_url} {p.age} {p.notes} {p.available}>"