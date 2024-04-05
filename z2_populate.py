import sqlite3

def create_database():
    conn = sqlite3.connect("QuizQA.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Finance (
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
        ("Finance", "What is the primary goal of financial management?", "A. Maximizing profits", "B. Maximizing shareholder wealth", "C. Minimizing expenses", "D. Maximizing revenue", "B. Maximizing shareholder wealth"),
        ("Finance", "What is the formula for calculating Return on Investment (ROI)?", "A. (Net Profit / Revenue) * 100", "B. (Net Profit / Investment) * 100", "C. (Investment / Net Profit) * 100", "D. (Revenue / Investment) * 100", "B. (Net Profit / Investment) * 100"),
        ("Finance", "What is the term used to describe the rate at which the general level of prices for goods and services is rising?", "A. Recession", "B. Deflation", "C. Inflation", "D. Depression", "C. Inflation"),
        ("Finance", "What does the acronym 'GAAP' stand for in accounting and finance?", "A. Generally Accepted Accounting Procedures", "B. Generally Accepted Auditing Principles", "C. Generally Accepted Accounting Principles", "D. Generally Approved Accounting Practices", "C. Generally Accepted Accounting Principles"),
        ("Finance", "What does the debt-to-equity ratio measure?", "A. A company's liquidity", "B. A company's profitability", "C. A company's financial leverage", "D. A company's asset management efficiency", "C. A company's financial leverage"),
        ("Finance", "Which financial statement reports a company's revenues and expenses over a period of time?", "A. Balance Sheet", "B. Income Statement", "C. Cash Flow Statement", "D. Statement of Retained Earnings", "B. Income Statement"),
        ("Finance", "What does the term 'diversification' refer to in finance?", "A. Investing in a single asset class", "B. Spreading investments across different assets", "C. Investing only in stocks", "D. Borrowing money to invest", "B. Spreading investments across different assets"),
        ("Finance", "What is the formula for calculating Net Present Value (NPV)?", "A. Present Value / Future Value", "B. Future Value / Present Value", "C. Present Value - Future Value", "D. Future Value - Present Value", "C. Present Value - Future Value"),
        ("Finance", "What does the term 'liquidity' refer to in finance?", "A. How quickly an asset can be converted into cash", "B. How much an asset is worth", "C. How risky an investment is", "D. How profitable a company is", "A. How quickly an asset can be converted into cash"),
        ("Finance", "What is the role of a financial manager in a company?", "A. To handle human resources", "B. To oversee marketing efforts", "C. To manage financial resources and risks", "D. To develop new products", "C. To manage financial resources and risks")
    ]

    cursor.executemany("INSERT INTO Finance (category, question, option1, option2, option3, option4, correct_answer) VALUES (?, ?, ?, ?, ?, ?, ?)", sample_questions)

    conn.commit()
    conn.close()
create_database()

