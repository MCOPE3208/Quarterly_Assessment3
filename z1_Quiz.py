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

        self.quiz_window = tk.Toplevel(master)
        self.quiz_window.title("Quiz Window")
        
        self.question_label = tk.Label(self.quiz_window, text=self.quiz_questions[self.current_question_index].question)
        self.question_label.pack()

        self.radio_vars = []
        self.radio_buttons = []
        for i, option in enumerate(self.quiz_questions[self.current_question_index].options):
            radio_var = tk.IntVar(value=-1)  # Use -1 to indicate no selection
            self.radio_vars.append(radio_var)
            radio_button = tk.Radiobutton(self.quiz_window, text=option, variable=self.radio_vars[self.current_question_index], value=i)
            radio_button.pack(anchor="w")
            self.radio_buttons.append(radio_button)

        self.feedback_label = tk.Label(self.quiz_window, text="", fg="black")
        self.feedback_label.pack(side="bottom", pady=5)

        self.submit_button = tk.Button(self.quiz_window, text="Submit Answer", command=self.check_answer)
        self.submit_button.pack(side="bottom", pady=10)
        
    def check_answer(self):
        selected_index = self.radio_vars[self.current_question_index].get()
        if selected_index == -1:
            messagebox.showerror("Error", "Please select an answer.")
            return

        selected_option = self.quiz_questions[self.current_question_index].options[selected_index].strip().lower()  # Get selected option
        correct_answer = self.quiz_questions[self.current_question_index].correct_answer.strip().lower()  # Get correct answer

        if selected_option == correct_answer:
            self.score += 1
            feedback = "Correct!"
            color = "green"
        else:
            feedback = f"Incorrect. The correct answer is: {self.quiz_questions[self.current_question_index].correct_answer}"
            color = "red"
        self.display_feedback(feedback, color)

    def display_feedback(self, feedback, color):
        self.feedback_label.config(text=feedback, fg=color)

        self.quiz_window.after(2000, self.next_question)

    def next_question(self):
        self.feedback_label.config(text="")  # Clear feedback
        self.current_question_index += 1
        if self.current_question_index < len(self.quiz_questions):
            self.update_question()
        elif not self.quiz_ended:  # Check if the quiz has ended
            self.feedback_label.config(text=f"Quiz Finished! Your score: {self.score}/{len(self.quiz_questions)}")
            self.quiz_ended = True  # Set the flag to indicate the quiz has ended
            self.back_button = tk.Button(self.quiz_window, text="Back to Category Selection", command=self.back_to_category_selection)
            self.back_button.pack(side="bottom", pady=10)

    def update_question(self):
        for radio_button in self.radio_buttons:
            radio_button.destroy()  # Destroy previous radio buttons

        self.question_label.config(text=self.quiz_questions[self.current_question_index].question)
        self.radio_vars.append(tk.IntVar(value=-1))  # Set default value to -1 for the new question
        for i, option in enumerate(self.quiz_questions[self.current_question_index].options):
            radio_button = tk.Radiobutton(self.quiz_window, text=option, variable=self.radio_vars[self.current_question_index], value=i)
            radio_button.pack(anchor="w")
            self.radio_buttons.append(radio_button)
    

if __name__ == "__main__":
    root = tk.Tk()
    root.mainloop()
