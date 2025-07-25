from flask import Flask, request, jsonify
from models import db, Customer, Loan, Payment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

@app.route('/lend', methods=['POST'])
def lend_money():
    data = request.json
    P = data['principal']
    N = data['years']
    R = data['rate']
    cid = data['customer_id']

    I = (P * N * R) / 100
    A = P + I
    emi = round(A / (N * 12), 2)

    loan = Loan(
        customer_id=cid, principal=P, rate=R, years=N,
        interest=I, total_amount=A, emi=emi
    )
    db.session.add(loan)
    db.session.commit()

    return jsonify({"total_amount": A, "monthly_emi": emi})

@app.route('/payment', methods=['POST'])
def make_payment():
    data = request.json
    payment = Payment(
        loan_id=data['loan_id'],
        amount=data['amount'],
        type=data['payment_type']
    )
    db.session.add(payment)
    db.session.commit()
    return jsonify({"message": "Payment recorded"})

@app.route('/ledger/<int:loan_id>', methods=['GET'])
def ledger(loan_id):
    loan = Loan.query.get(loan_id)
    payments = Payment.query.filter_by(loan_id=loan_id).all()
    total_paid = sum(p.amount for p in payments)
    emi_left = int((loan.total_amount - total_paid) / loan.emi)
    emi_left = max(0, emi_left)

    return jsonify({
        "loan_id": loan_id,
        "monthly_emi": loan.emi,
        "payments": [
            {"amount": p.amount, "type": p.type, "date": p.date} for p in payments
        ],
        "total_paid": total_paid,
        "balance": round(loan.total_amount - total_paid, 2),
        "emi_left": emi_left
    })

@app.route('/account-overview/<int:customer_id>', methods=['GET'])
def account_overview(customer_id):
    loans = Loan.query.filter_by(customer_id=customer_id).all()
    result = []
    for loan in loans:
        payments = Payment.query.filter_by(loan_id=loan.id).all()
        total_paid = sum(p.amount for p in payments)
        emi_left = int((loan.total_amount - total_paid) / loan.emi)
        emi_left = max(0, emi_left)
        result.append({
            "loan_id": loan.id,
            "principal": loan.principal,
            "total_amount": loan.total_amount,
            "interest": loan.interest,
            "emi": loan.emi,
            "total_paid": total_paid,
            "emi_left": emi_left
        })
    return jsonify(result)

import os

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host='0.0.0.0', port=port, debug=True)
