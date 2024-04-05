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

    # Add sample questions for testing
    sample_questions = [
        ("Taxation", "What is the main purpose of taxation?", "A. Generate revenue", "B. Discourage consumption", "C. Encourage saving", "D. None of the above", "A. Generate revenue"),
        ("Taxation", "Which of the following is a direct tax?", "A. Value Added Tax (VAT)", "B. Sales Tax", "C. Income Tax", "D. Excise Duty", "C. Income Tax"),
        ("Taxation", "Which of the following taxes is based on the value of real estate?", "A. Property Tax", "B. Excise Tax", "C. Sales Tax", "D. Income Tax", "A. Property Tax"),
        ("Taxation", "Which tax is levied on the transfer of property by one individual to another?", "A. Estate Tax", "B. Excise Tax", "C. Value Added Tax (VAT)", "D. Corporate Tax", "A. Estate Tax"),
        ("Taxation", "What is the name of the tax levied on the profits of corporations?", "A. Income Tax", "B. Capital Gains Tax", "C. Corporate Tax", "D. Property Tax", "C. Corporate Tax"),
        ("Taxation", "Which of the following is a type of consumption tax?", "A. Excise Tax", "B. Income Tax", "C. Payroll Tax", "D. Property Tax", "A. Excise Tax"),
        ("Taxation", "Which tax is imposed on the earnings of individuals and businesses within a specific jurisdiction?", "A. Property Tax", "B. Income Tax", "C. Sales Tax", "D. Estate Tax", "B. Income Tax"),
        ("Taxation", "What type of tax is charged on the income of individuals and corporations by the government?", "A. Property Tax", "B. Income Tax", "C. Sales Tax", "D. Excise Tax", "B. Income Tax"),
        ("Taxation", "What tax is levied on the transfer of money or property by inheritance?", "A. Sales Tax", "B. Estate Tax", "C. Excise Tax", "D. Corporate Tax", "B. Estate Tax"),
        ("Taxation", "What tax is paid directly by the person or entity to the imposing entity?", "A. Indirect Tax", "B. Direct Tax", "C. Progressive Tax", "D. Regressive Tax", "B. Direct Tax")
    ]

    cursor.executemany("INSERT INTO Taxation (category, question, option1, option2, option3, option4, correct_answer) VALUES (?, ?, ?, ?, ?, ?, ?)", sample_questions)
    conn.commit()
    conn.close()
create_database()

