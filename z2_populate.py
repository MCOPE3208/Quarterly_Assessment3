import sqlite3

def create_database():
    conn = sqlite3.connect("QuizQA.db")
    cursor = conn.cursor()

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

    sample_questions = [
        ("BusinessAnalytics","What is Business Analytics?", "A. The study of business functions", "B. The use of data analysis tools and techniques to make informed business decisions", "C. The process of creating business strategies", "D. The implementation of marketing campaigns", "B. The use of data analysis tools and techniques to make informed business decisions"),
        ("BusinessAnalytics","Which statistical technique is used to identify relationships between variables?", "A. Descriptive statistics", "B. Inferential statistics", "C. Correlation analysis", "D. Regression analysis", "C. Correlation analysis"),
        ("BusinessAnalytics","What is the purpose of data visualization in business analytics?", "A. To make data easier to understand", "B. To make data more complex", "C. To confuse stakeholders", "D. To reduce data accuracy", "A. To make data easier to understand"),
        ("BusinessAnalytics","Which of the following is an example of descriptive analytics?", "A. Predictive modeling", "B. Dashboard reporting", "C. Market basket analysis", "D. Text mining", "B. Dashboard reporting"),
        ("BusinessAnalytics","What does ROI stand for in the context of business analytics?", "A. Return on Investment", "B. Return on Income", "C. Revenue on Investment", "D. Ratio of Input", "A. Return on Investment"),
        ("BusinessAnalytics","Which data visualization tool allows users to create interactive and shareable dashboards?", "A. Tableau", "B. Excel", "C. PowerPoint", "D. Google Sheets", "A. Tableau"),
        ("BusinessAnalytics","What is the purpose of predictive analytics?", "A. To analyze past data", "B. To predict future outcomes", "C. To summarize data", "D. To create reports", "B. To predict future outcomes"),
        ("BusinessAnalytics","Which statistical measure is used to describe the spread of data around the mean?", "A. Mean", "B. Median", "C. Mode", "D. Standard deviation", "D. Standard deviation"),
        ("BusinessAnalytics","What is the goal of prescriptive analytics?", "A. To describe what happened", "B. To predict what will happen", "C. To prescribe the best course of action", "D. To summarize data", "C. To prescribe the best course of action"),
        ("BusinessAnalytics","Which type of analysis is used to determine the likelihood of a certain event occurring?", "A. Predictive analysis", "B. Descriptive analysis", "C. Prescriptive analysis", "D. Inferential analysis", "A. Predictive analysis")
    ]

    cursor.executemany("INSERT INTO BusinessAnalytics (category, question, option1, option2, option3, option4, correct_answer) VALUES (?, ?, ?, ?, ?, ?, ?)", sample_questions)
    
    conn.commit()
    conn.close()
create_database()

