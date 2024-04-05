import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class QuizQuestion:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Category Selection")
        
        self.category_var = tk.StringVar()
        
        self.label = tk.Label(master, text="Select a category:")
        self.label.pack()
        
        self.combo_box = ttk.Combobox(master, textvariable=self.category_var, values=[
            "Taxation", "Finance", "Business App Development", 
            "Cost Accounting", "Financial Accounting", "Business Analytics"
        ])
        self.combo_box.pack()
        
        self.start_button = tk.Button(master, text="Start Quiz Now", command=self.start_quiz)
        self.start_button.pack()

    def start_quiz(self):
        category = self.category_var.get()
        if category:
            self.combo_box.set("")  # Reset the combo box
            self.master.withdraw()  # Hide the category selection window
            quiz_questions = self.load_questions(category)
            QuizWindow(quiz_questions, category, self.master)   

    def load_questions(self, category):
        conn = sqlite3.connect("QuizQA.db")
        cursor = conn.cursor()

        cursor.execute(f"SELECT question, option1, option2, option3, option4, correct_answer FROM {category.replace(' ', '')} ORDER BY RANDOM() LIMIT 10")      
        questions = cursor.fetchall()
        quiz_questions = []
        for question in questions:
            question_text, option1, option2, option3, option4, correct_answer = question
            options = [option1, option2, option3, option4]
            quiz_questions.append(QuizQuestion(question_text, options, correct_answer))
    
        conn.close()
        return quiz_questions

class QuizWindow:
    def __init__(self, quiz_questions, category, master):
        self.quiz_questions = quiz_questions
        self.category = category
        self.master = master
        self.current_question_index = 0
        self.score = 0
        self.quiz_ended = False  # Flag to indicate if the quiz has ended
        

if __name__ == "__main__":
    root = tk.Tk()
    root.mainloop()
