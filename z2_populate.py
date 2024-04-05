import sqlite3

def create_database():
    conn = sqlite3.connect("QuizQA.db")
    cursor = conn.cursor()

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

    sample_questions = [
        ("CostAccounting","What is the main objective of cost accounting?", "A. Profit maximization", "B. Cost minimization", "C. Revenue maximization", "D. Market share maximization", "B. Cost minimization"),
        ("CostAccounting","Which cost is also known as traceable cost?", "A. Direct cost", "B. Indirect cost", "C. Fixed cost", "D. Variable cost", "A. Direct cost"),
        ("CostAccounting","What is the formula to calculate total manufacturing cost?", "A. Direct materials + Direct labor + Variable manufacturing overhead", "B. Direct materials + Direct labor + Fixed manufacturing overhead", "C. Direct materials + Variable manufacturing overhead", "D. Direct labor + Fixed manufacturing overhead", "A. Direct materials + Direct labor + Variable manufacturing overhead"),
        ("CostAccounting","What is the term for the cost incurred to acquire or produce a product?", "A. Manufacturing cost", "B. Selling cost", "C. Administrative cost", "D. Period cost", "A. Manufacturing cost"),
        ("CostAccounting","What is the formula for calculating contribution margin per unit?", "A. Selling price - Variable cost per unit", "B. Selling price + Variable cost per unit", "C. Fixed cost per unit - Variable cost per unit", "D. Fixed cost per unit / Variable cost per unit", "A. Selling price - Variable cost per unit"),
        ("CostAccounting","Which method allocates overhead costs based on the actual usage of resources?", "A. Traditional costing", "B. Activity-based costing", "C. Direct costing", "D. Absorption costing", "B. Activity-based costing"),
        ("CostAccounting","What is the term for the rate used to apply manufacturing overhead to units produced?", "A. Predetermined overhead rate", "B. Actual overhead rate", "C. Variable overhead rate", "D. Fixed overhead rate", "A. Predetermined overhead rate"),
        ("CostAccounting","Which costing method allocates fixed manufacturing overhead costs evenly across all units produced?", "A. Variable costing", "B. Absorption costing", "C. Job costing", "D. Process costing", "B. Absorption costing"),
        ("CostAccounting","What is the formula to calculate the cost of goods manufactured?", "A. Beginning Work in Process Inventory + Total Manufacturing Costs - Ending Work in Process Inventory", "B. Beginning Finished Goods Inventory + Cost of Goods Sold - Ending Finished Goods Inventory", "C. Beginning Raw Materials Inventory + Purchases - Ending Raw Materials Inventory", "D. Beginning Work in Process Inventory + Direct Materials Used + Direct Labor + Manufacturing Overhead", "D. Beginning Work in Process Inventory + Direct Materials Used + Direct Labor + Manufacturing Overhead"),
        ("CostAccounting","Which type of cost changes in direct proportion to changes in the level of activity?", "A. Variable cost", "B. Fixed cost", "C. Mixed cost", "D. Step cost", "A. Variable cost")
    ]

    cursor.executemany("INSERT INTO CostAccounting (category, question, option1, option2, option3, option4, correct_answer) VALUES (?, ?, ?, ?, ?, ?, ?)", sample_questions)
    
    conn.commit()
    conn.close()
create_database()

