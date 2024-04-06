# Quarterly_Assessment3

## Overview
The program is a simple quiz application built using Python and Tkinter, a standard GUI toolkit for Python. The main purpose of the program is to provide users with a quiz experience where they can select a category of questions and answer them one by one. The user interface consists of a category selection window and a quiz window.
To run the program, users only need to use the file named "z1_Quiz.py". When they run this file, a window will appear prompting them to select a quiz category from a dropdown menu. The available categories include Taxation, Finance, Business App Development, Cost Accounting, Financial Accounting, and Business Analytics. Once the user selects a category and clicks the "Start Quiz Now" button, a new window will open containing the quiz questions for the selected category.
In the quiz window, users will see a question along with multiple-choice options. They can select an option by clicking on the radio button next to it and then click the "Submit Answer" button to check their answer. If they don't select an option before submitting, an error message will prompt them to do so. After submitting an answer, the program will provide immediate feedback indicating whether the answer was correct or incorrect. The user's score will also be displayed.
Once the user completes the quiz, a message will appear indicating that the quiz has finished, along with their final score. At this point, a button labeled "Back to Category Selection" will appear at the bottom of the window. Clicking this button will close the quiz window and return the user to the category selection window, allowing them to choose a new category and start a new quiz if desired.

## File Overview

z1_Quiz.py : The z1_Quiz.py file is the main program for a quiz application, allowing users to select quiz categories, answer questions, receive feedback, and view final scores. It provides a graphical user interface for an interactive quiz experience, all contained within a single Python script 

z2_populate.py : The z2_populate.py file is responsible for populating the database (QuizQA.db) with questions, options, and correct answers for various quiz categories, such as Taxation, Finance, and Business App Development, facilitating the availability of quiz content for the main application.

QuizQA.db : Inside the QuizQA.db file, there are tables that store all the quiz questions and related information, such as the category of each question, the question itself, the multiple-choice options, and the correct answer.

read.py : The file that reads the database and is responsible for accessing the quiz questions stored in the database and presenting them to you