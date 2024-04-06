import sqlite3

def create_database():
    conn = sqlite3.connect("QuizQA.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Taxation (
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

    # Add sample questions for taxation
    sample_questions = [
        #("Taxation", "What is the main purpose of taxation?", "A. Generate revenue", "B. Discourage consumption", "C. Encourage saving", "D. None of the above", "A. Generate revenue"),
        ]

    cursor.executemany("INSERT INTO Taxation (category, question, option1, option2, option3, option4, correct_answer) VALUES (?, ?, ?, ?, ?, ?, ?)", sample_questions)


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

# Add sample questions for Finance
    sample_questions = [
        #("Finance", "What is the primary goal of financial management?", "A. Maximizing profits", "B. Maximizing shareholder wealth", "C. Minimizing expenses", "D. Maximizing revenue", "B. Maximizing shareholder wealth"),
        ]

    cursor.executemany("INSERT INTO Finance (category, question, option1, option2, option3, option4, correct_answer) VALUES (?, ?, ?, ?, ?, ?, ?)", sample_questions)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS BusinessAppDevelopment (
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

# Add sample questions for BusinessAppDevelopment
    sample_questions = [
        #("BusinessAppDevelopment","What is the primary programming language used for developing Android apps?", "A. Java", "B. Python", "C. Swift", "D. JavaScript", "A. Java"),
        ]

    cursor.executemany("INSERT INTO BusinessAppDevelopment (category, question, option1, option2, option3, option4, correct_answer) VALUES (?, ?, ?, ?, ?, ?, ?)", sample_questions)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS CostAccounting (
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

# Add sample questions for CostAccounting
    sample_questions = [
        #("CostAccounting","What is the main objective of cost accounting?", "A. Profit maximization", "B. Cost minimization", "C. Revenue maximization", "D. Market share maximization", "B. Cost minimization"),
        ]

    cursor.executemany("INSERT INTO CostAccounting (category, question, option1, option2, option3, option4, correct_answer) VALUES (?, ?, ?, ?, ?, ?, ?)", sample_questions)
    
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

# Add sample questions for FinancialAccounting
    sample_questions = [
        #("FinancialAccounting","What is the accounting equation?", "A. Assets = Liabilities - Equity", "B. Assets = Liabilities + Equity", "C. Assets = Liabilities / Equity", "D. Assets = Liabilities * Equity", "B. Assets = Liabilities + Equity"),
        ]

    cursor.executemany("INSERT INTO FinancialAccounting (category, question, option1, option2, option3, option4, correct_answer) VALUES (?, ?, ?, ?, ?, ?, ?)", sample_questions)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS BusinessAnalytics (
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

# Add sample questions for BusinessAnalytics
    sample_questions = [
        #("BusinessAnalytics","What is Business Analytics?", "A. The study of business functions", "B. The use of data analysis tools and techniques to make informed business decisions", "C. The process of creating business strategies", "D. The implementation of marketing campaigns", "B. The use of data analysis tools and techniques to make informed business decisions"),
        ]
    cursor.executemany("INSERT INTO BusinessAnalytics (category, question, option1, option2, option3, option4, correct_answer) VALUES (?, ?, ?, ?, ?, ?, ?)", sample_questions)
    
    
    conn.commit()
    conn.close()
create_database()

