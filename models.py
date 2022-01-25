"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

Default_Image_url = 'https://freepikpsd.com/file/2019/10/default-profile-image-png-1-Transparent-Images.png'

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class User(db.Model):
    """User."""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String,
                     nullable=False,
                     unique=False)
    last_name = db.Column(db.String,
                     nullable=False,
                     unique=False)
    image_url = db.Column(db.String,
                     nullable=True,
                     default=Default_Image_url)

    @property
    def full_name(self):
        """Returns the full name"""

        return f"{self.first_name} {self.last_name}"