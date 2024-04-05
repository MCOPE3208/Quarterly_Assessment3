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
        


if __name__ == "__main__":
    root = tk.Tk()
    root.mainloop()
