from app import db

class User(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(160), unique=True, nullable=False)
    phone = db.Column(db.String(100))
    password = db.Column(db.String(60), nullable=False)


    def __init__(self, name, email, phone, password):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password