from flask_mysqldb import MySQL

def init_db(app):
    mysql = MySQL(app)
    
    # Create tables if they don't exist
    cur = mysql.connection.cursor()
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        password VARCHAR(100) NOT NULL
    )
    """)
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS loan_applications (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        BankruptcyHistory BOOLEAN,
        TotalDebtToIncomeRatio FLOAT,
        DebtToIncomeRatio FLOAT,
        NetWorth FLOAT,
        AnnualIncome FLOAT,
        MonthlyIncome FLOAT,
        RiskScore FLOAT,
        LoanApproved BOOLEAN,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """)
    
    mysql.connection.commit()
    cur.close()