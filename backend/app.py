from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
import pickle
import os

app = Flask(__name__)
CORS(app)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'loan_approval'
mysql = MySQL(app)

# Load ML models
rf_model = pickle.load(open('D:/Loan Approval/rf_regression_model.pkl', 'rb'))
logistic_model = pickle.load(open('D:/Loan Approval/logistic_regression_model.pkl', 'rb'))

@app.route('/')
def home():
    return "Loan Approval System Backend"

@app.route('/predict_risk', methods=['POST'])
def predict_risk():
    data = request.json
    features = [
        data['BankruptcyHistory'],
        data['TotalDebtToIncomeRatio'],
        data['DebtToIncomeRatio'],
        data['NetWorth'],
        data['AnnualIncome'],
        data['MonthlyIncome']
    ]
    risk_score = rf_model.predict([features])[0]
    return jsonify({'risk_score': float(risk_score)})

@app.route('/predict_approval', methods=['POST'])
def predict_approval():
    data = request.json
    features = [
        data['BankruptcyHistory'],
        data['TotalDebtToIncomeRatio'],
        data['DebtToIncomeRatio'],
        data['NetWorth'],
        data['AnnualIncome'],
        data['MonthlyIncome'],
        data['RiskScore']
    ]
    approval = logistic_model.predict([features])[0]
    return jsonify({'approved': bool(approval)})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE email = %s AND password = %s", 
               (data['email'], data['password']))
    user = cur.fetchone()
    cur.close()
    if user:
        return jsonify({'success': True, 'user_id': user[0]})
    return jsonify({'success': False})

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
               (data['name'], data['email'], data['password']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)