"""Seed file to make sample data for db"""

from models import User, db
from app import app

#Create all tables
db.drop_all()
db.create_all()

river = User(first_name = "River", last_name = "Bottom")
joaquin = User(first_name = "Joaquin", last_name="Pheonix", image_url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.gq-magazine.co.uk%2Fculture%2Farticle%2Fjoaquin-phoenix-life-movies&psig=AOvVaw0F748HqxFA0PQRFQblPjJD&ust=1643575609033000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCOCl-Mjq1_UCFQAAAAAdAAAAABAD")
summer = User(first_name = "Summer", last_name="Winter")
octavia = User(first_name = "Octavia", last_name="Spencer")

db.session.add_all([river, joaquin, summer, octavia])

db.session.commit()