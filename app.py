from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)

class BetaUser(db.Model):
    __tablename__ = 'beta_users'
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(50), nullable=False)
    last = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    charity = db.Column(db.Boolean(), nullable=False)
    sponsor = db.Column(db.Boolean(), nullable=False)
    created = db.Column(db.DateTime(), nullable=False)

    def __init__(self, first, last, email, charity, sponsor, created):
        self.first = first
        self.last = last
        self.email = email
        self.charity = charity
        self.sponsor = sponsor
        self.created = created

    def __repr__(self):
        return '<User %r>' % self.first


@app.route('/')
def home():
    return app.config['SQLALCHEMY_DATABASE_URI']

if __name__ == '__main__':
    app.run()
