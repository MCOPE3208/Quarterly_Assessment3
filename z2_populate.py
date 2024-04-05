import sqlite3

def create_database():
    conn = sqlite3.connect("QuizQA.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS FinancialAccounting (
        id INTEGER PRIMARY KEY,
        category TEXT,
        question TEXT,
        option1 TEXT,
        option2 TEXT,
        option3 TEXT,
        option4 TEXT,
        correct_answer TEXT
    )
    """)

    sample_questions = [
        ("FinancialAccounting","What is the accounting equation?", "A. Assets = Liabilities - Equity", "B. Assets = Liabilities + Equity", "C. Assets = Liabilities / Equity", "D. Assets = Liabilities * Equity", "B. Assets = Liabilities + Equity"),
        ("FinancialAccounting","Which financial statement shows a company's revenues and expenses over a period of time?", "A. Balance sheet", "B. Income statement", "C. Statement of cash flows", "D. Statement of retained earnings", "B. Income statement"),
        ("FinancialAccounting","What is the term for the amount earned from sales of goods or services?", "A. Profit", "B. Revenue", "C. Expense", "D. Liability", "B. Revenue"),
        ("FinancialAccounting","Which accounting principle requires that expenses be recorded in the same period as the revenues they help to generate?", "A. Matching principle", "B. Revenue recognition principle", "C. Going concern principle", "D. Conservatism principle", "A. Matching principle"),
        ("FinancialAccounting","What is the term for the cost of goods sold by a company during a specific period?", "A. Gross profit", "B. Operating income", "C. Net income", "D. Cost of goods sold (COGS)", "D. Cost of goods sold (COGS)"),
        ("FinancialAccounting","Which financial statement reports a company's assets, liabilities, and shareholders' equity at a specific point in time?", "A. Balance sheet", "B. Income statement", "C. Statement of cash flows", "D. Statement of retained earnings", "A. Balance sheet"),
        ("FinancialAccounting","What is the formula to calculate net income?", "A. Revenue - Expenses", "B. Revenue + Expenses", "C. Assets - Liabilities", "D. Liabilities - Equity", "A. Revenue - Expenses"),
        ("FinancialAccounting","Which accounting principle states that assets should be recorded at their original cost?", "A. Historical cost principle", "B. Matching principle", "C. Revenue recognition principle", "D. Full disclosure principle", "A. Historical cost principle"),
        ("FinancialAccounting","What is the term for the profit a company earns before deducting taxes and interest expenses?", "A. Gross profit", "B. Operating profit", "C. Net profit", "D. Earnings before interest and taxes (EBIT)", "B. Operating profit"),
        ("FinancialAccounting","What is the formula for calculating return on assets (ROA)?", "A. Net income / Total assets", "B. Net income / Shareholders' equity", "C. Total assets / Net income", "D. Total assets / Shareholders' equity", "A. Net income / Total assets")
    ]

    cursor.executemany("INSERT INTO FinancialAccounting (category, question, option1, option2, option3, option4, correct_answer) VALUES (?, ?, ?, ?, ?, ?, ?)", sample_questions)
    
    conn.commit()
    conn.close()
create_database()

