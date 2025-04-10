# Loan Approval System

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

A full-stack web application that predicts loan eligibility using machine learning, featuring:
- Risk score calculation with Random Forest regression
- Loan approval prediction with Logistic Regression
- Secure user authentication
- Minimalist black-and-white UI

## 🚀 Features

- **Dual-stage ML Pipeline**:
  - Risk Score prediction based on financial parameters
  - Loan Approval classification using risk score + financial data
- **User Management**:
  - Secure registration/login system
  - Application history tracking
- **Responsive Dashboard**:
  - Real-time prediction results
  - Form validation and error handling

## 🛠️ Tech Stack

**Frontend**:
- React.js
- React Router
- Axios for API calls

**Backend**:
- Python Flask
- Flask-MySQLdb
- Flask-CORS

**Machine Learning**:
- scikit-learn
- Random Forest Regressor
- Logistic Regression Classifier

**Database**:
- MySQL

## 📦 Installation

### Prerequisites
- Python 3.8+
- Node.js 16+
- MySQL Server

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
# Configure MySQL credentials in app.py
python models.py  # Initialize database
python app.py    # Start Flask server (http://localhost:5000)
```


# Frontend Setup
```bash
Copy
cd frontend
npm install
npm start  # Starts React app (http://localhost:3000)
```
### 🌐 API Endpoints
Endpoint	Method	Description
/predict_risk	POST	Calculate risk score
/predict_approval	POST	Check loan eligibility
/register	POST	User registration
/login	POST	User authentication
