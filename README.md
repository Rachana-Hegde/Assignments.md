# 🏦 Bank Loan Management System – RESTful API (Flask + SQLite)

This project is a backend loan management system built using **Python Flask** and **SQLite**, designed to simulate how a bank lends money to customers, tracks payments, and manages loan accounts. Developed as part of an **internship assignment at AgetWare**, it demonstrates RESTful design principles, real-world calculations, and data persistence.

---

## 🚀 Features

* 💰 **LEND**: Assign loans to customers with interest and EMI generation.
* 💳 **PAYMENT**: Accept EMI or lump sum payments, reduce loan balance.
* 📒 **LEDGER**: View full loan transaction history, EMI left, and outstanding balance.
* 🧾 **ACCOUNT OVERVIEW**: Summary of all loans taken by a customer.
* 🛠️ **Simple RESTful API**: Easily testable using Postman, curl, or Thunder Client.

---

## 📌 Technologies Used

* **Backend:** Python, Flask
* **Database:** SQLite with SQLAlchemy ORM
* **API Testing:** Postman or Thunder Client
* **Environment:** Cross-platform (Windows/Linux/Mac)
* **Deployment:** Local development server

---

## 🧠 How It Works

1. **LEND API** accepts loan data (principal, rate, years), calculates:

   * 📈 Simple Interest: `I = P × N × R / 100`
   * 💵 Total Amount: `A = P + I`
   * 📆 EMI: `A / (N × 12)`
2. **PAYMENT API** deducts payments from loan balance.
3. **LEDGER API** shows all payments + remaining balance.
4. **ACCOUNT OVERVIEW API** lists all loans with status for a customer.

---

## 📥 Installation

```bash
git clone https://github.com/your-username/bank-loan-system.git
cd bank-loan-system
python -m venv venv
venv\Scripts\activate        # On Windows
# OR
source venv/bin/activate     # On Mac/Linux
pip install -r requirements.txt
python app.py
```

> 🏃‍♂️ App will run at: `http://127.0.0.1:5000/`

---

## 📬 API Endpoints

### 🔹 POST `/lend`

**Description:** Assign a loan to a customer.

```json
{
  "customer_id": 1,
  "principal": 100000,
  "years": 2,
  "rate": 10
}
```

**Response:**

```json
{
  "total_amount": 120000.0,
  "monthly_emi": 5000.0
}
```

---

### 🔹 POST `/payment`

**Description:** Make a payment (EMI or LUMP\_SUM).

```json
{
  "loan_id": 1,
  "amount": 10000,
  "payment_type": "LUMP_SUM"
}
```

---

### 🔹 GET `/ledger/<loan_id>`

**Description:** View all payments made for a specific loan.

**Response:**

```json
{
  "loan_id": 1,
  "monthly_emi": 5000.0,
  "payments": [
    {"amount": 10000, "type": "LUMP_SUM", "date": "..."}
  ],
  "total_paid": 10000,
  "balance": 110000,
  "emi_left": 22
}
```

---

### 🔹 GET `/account-overview/<customer_id>`

**Description:** See all loans for a customer.

**Response:**

```json
[
  {
    "loan_id": 1,
    "principal": 100000,
    "total_amount": 120000,
    "interest": 20000,
    "emi": 5000,
    "total_paid": 10000,
    "emi_left": 22
  }
]
```

---

## 📂 Project Structure

```
bank-loan-system/
│
├── app.py                 # Main Flask app
├── models.py              # SQLAlchemy models
├── requirements.txt       # Required Python packages
├── README.md              # Project documentation
```

---

## ✅ How to Use

1. Run the Flask server using `python app.py`.
2. Use Postman or Thunder Client to call the `/lend`, `/payment`, `/ledger`, and `/account-overview` APIs.
3. Track loan balances, EMIs, and transactions for different customers.

---

## 📎 Sample Customer (Optional)

To make testing easier, `customer_id: 1` is preloaded when the app runs. You can extend this by adding a `POST /register-customer` endpoint if needed.

---

## 🔐 Notes

* This project uses **Simple Interest** logic for clarity.
* All calculations are rounded for simplicity.
* Not intended for production deployment.
* Project created for **educational/demo** purposes during internship at **AgetWare**.

---

## 📄 License

This project is licensed under the **MIT License**.
Feel free to use, modify, and share for learning purposes.

---

## 📬 Contact  

For any inquiries or feedback, feel free to reach out:    
🔗 **GitHub**: [Rachana-Hegde](https://github.com/Rachana-Hegde)  
