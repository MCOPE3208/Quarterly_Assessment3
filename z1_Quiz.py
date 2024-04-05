import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class QuizQuestion:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer


if __name__ == "__main__":
    root = tk.Tk()
    root.mainloop()
