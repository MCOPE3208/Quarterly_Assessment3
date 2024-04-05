import sqlite3

def read_entries():
    conn = sqlite3.connect("QuizQA.db")
    cursor = conn.cursor()
#whatever table you want to look at use its name instead of finance
    cursor.execute("SELECT * FROM Finance")
    entries = cursor.fetchall()
    for entry in entries:
        print(entry)
    
    conn.close()

if __name__ == "__main__":
    read_entries()
