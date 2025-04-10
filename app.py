from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the saved linear regression model
model_path = r"D:\Loan Approval\linear_regression_model.pkl"
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Home route with form
@app.route('/')
def home():
    return render_template('index.html')

# Route to make predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect form inputs from the user
        features = [float(request.form[feature]) for feature in [
            'Age', 'AnnualIncome', 'CreditScore', 'EmploymentStatus', 
            'EducationLevel', 'Experience', 'LoanAmount', 'LoanDuration', 
            'MaritalStatus', 'NumberOfDependents', 'HomeOwnershipStatus', 
            'MonthlyDebtPayments', 'CreditCardUtilizationRate', 
            'NumberOfOpenCreditLines', 'NumberOfCreditInquiries', 
            'DebtToIncomeRatio', 'BankruptcyHistory', 'LoanPurpose', 
            'PreviousLoanDefaults', 'PaymentHistory', 'LengthOfCreditHistory', 
            'SavingsAccountBalance', 'CheckingAccountBalance', 'TotalAssets', 
            'TotalLiabilities', 'MonthlyIncome', 'UtilityBillsPaymentHistory', 
            'JobTenure', 'NetWorth', 'BaseInterestRate', 'InterestRate', 
            'MonthlyLoanPayment', 'TotalDebtToIncomeRatio'
        ]]
        
        # Convert features into a NumPy array
        features_array = np.array([features])

        # Predict risk score using the loaded model
        risk_score = model.predict(features_array)[0]

        # Display result on the page
        return render_template('index.html', prediction_text=f'Predicted Risk Score: {risk_score:.2f}')
    
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
