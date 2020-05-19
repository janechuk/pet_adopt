"""Seed file for adoption agency app"""
from models import Pet, db
from app import app



#creat all tables
db.drop_all()
db.create_all()


p1 = Pet(name="Snargle", species="cat", photo_url="https://images.unsplash.com/photo-1535930891776-0c2dfb7fda1a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60", age=3, notes="Lorem lorem ipsum", available=True)
p2 = Pet(name="Porcheta", species="cat", photo_url="https://images.unsplash.com/photo-1561984142-7fabd0b4c9b4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60", age=2, notes="Lorem lorem ipsum", available=True)
p3 = Pet(name="Bosco", species="dog", photo_url="https://images.unsplash.com/flagged/photo-1583958211970-af3e1596ef32?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60", age=4, notes="Lorem lorem ipsum", available=False)
p4 = Pet(name="Chewy", species="dog", photo_url="https://images.unsplash.com/photo-1566489564594-f2163930c034?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60", age=1, notes="Lorem lorem ipsum", available=True)



db.session.add_all([p1, p2, p3, p4])
db.session.commit()