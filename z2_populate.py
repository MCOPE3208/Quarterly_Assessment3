import sqlite3

def create_database():
    conn = sqlite3.connect("QuizQA.db")
    cursor = conn.cursor()

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

    sample_questions = [
        ("BusinessAppDevelopment","What is the primary programming language used for developing Android apps?", "A. Java", "B. Python", "C. Swift", "D. JavaScript", "A. Java"),
        ("BusinessAppDevelopment","Which of the following is not a commonly used database management system for business applications?", "A. MySQL", "B. SQLite", "C. Oracle", "D. MongoDB", "D. MongoDB"),
        ("BusinessAppDevelopment","Which framework is commonly used for building web applications with Python?", "A. Flask", "B. Django", "C. Express.js", "D. Ruby on Rails", "B. Django"),
        ("BusinessAppDevelopment","What does MVC stand for in the context of software development?", "A. Model-View-Coding", "B. Model-View-Component", "C. Model-View-Controller", "D. Model-View-Command", "C. Model-View-Controller"),
        ("BusinessAppDevelopment","Which programming language is commonly used for building cross-platform mobile apps?", "A. Java", "B. Swift", "C. Kotlin", "D. JavaScript", "D. JavaScript"),
        ("BusinessAppDevelopment","What does API stand for in the context of software development?", "A. Application Programming Interface", "B. Advanced Programming Interface", "C. Application Process Integration", "D. Advanced Program Instruction", "A. Application Programming Interface"),
        ("BusinessAppDevelopment","Which of the following is not an example of a cloud computing service?", "A. Amazon Web Services (AWS)", "B. Google Cloud Platform (GCP)", "C. Microsoft Excel", "D. IBM Cloud", "C. Microsoft Excel"),
        ("BusinessAppDevelopment","Which design pattern is commonly used for managing state in front-end applications?", "A. Singleton", "B. Observer", "C. Factory", "D. Redux", "D. Redux"),
        ("BusinessAppDevelopment","What is the purpose of version control systems like Git in software development?", "A. Testing code", "B. Collaborating with other developers", "C. Documenting requirements", "D. Writing code", "B. Collaborating with other developers"),
        ("BusinessAppDevelopment","What is the primary function of a RESTful API?", "A. Storing data", "B. Creating user interfaces", "C. Handling HTTP requests", "D. Processing payment transactions", "C. Handling HTTP requests")
    ]

    cursor.executemany("INSERT INTO BusinessAppDevelopment (category, question, option1, option2, option3, option4, correct_answer) VALUES (?, ?, ?, ?, ?, ?, ?)", sample_questions)
    
    conn.commit()
    conn.close()
create_database()

