from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    principal = db.Column(db.Float, nullable=False)
    rate = db.Column(db.Float, nullable=False)
    years = db.Column(db.Float, nullable=False)
    interest = db.Column(db.Float)
    total_amount = db.Column(db.Float)
    emi = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loan_id = db.Column(db.Integer, db.ForeignKey('loan.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(20))  # EMI or LUMP_SUM
    date = db.Column(db.DateTime, default=datetime.utcnow)