import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.filedialog import askopenfile

import csv

imported_data = ""  # Store the imported data

def import_data():
    # Open a CSV file dialog and get the selected file
    file = askopenfile(mode='r', filetypes=[('CSV Files', '*.csv')])

    if file:
    
        # Clear the imported_text widget
        imported_text.delete(1.0, tk.END)
        
        # Use csv.reader to read the CSV file
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        
        for row in csv_reader:
            sid = row[0]
            first_name = row[1]
            last_name = row[2]
            email = row[3]
            homeworks = [row[i] for i in range(4, 7) if row[i] != '']
            quizzes = [row[i] for i in range(7, 11) if row[i] != '']
            midterm = row[11] if row[11] != '' else '0'
            final = row[12] if row[12] != '' else '0'

            # Calculate the grade based on your criteria
            total_score = (
                (sum(float(hw) for hw in homeworks) / 3) * 0.2 +
                (sum(float(quiz) for quiz in quizzes) / 4) * 0.2 +
                float(midterm) * 0.3 +
                float(final) * 0.3
            )

            if total_score >= 90:
                grade = 'A'
            elif 80 <= total_score < 90:
                grade = 'B'
            elif 70 <= total_score < 80:
                grade = 'C'
            elif 60 <= total_score < 70:
                grade = 'D'
            else:
                grade = 'F'

            # Display the student information in the text widget
            imported_text.insert(tk.END, f"SID: {sid}\n")
            imported_text.insert(tk.END, f"FirstName: {first_name}\n")
            imported_text.insert(tk.END, f"LastName: {last_name}\n")
            imported_text.insert(tk.END, f"Email: {email}\n")
            imported_text.insert(tk.END, f"Homeworks: {', '.join(homeworks)}\n")
            imported_text.insert(tk.END, f"Quizzes: {', '.join(quizzes)}\n")
            imported_text.insert(tk.END, f"MidtermExam: {midterm}\n")
            imported_text.insert(tk.END, f"FinalExam: {final}\n")
            imported_text.insert(tk.END, f"Grade: {grade}\n")
            imported_text.insert(tk.END, "\n")  # Add a blank line to separate students


def display_imported_data():
    # Clear the text box and insert the imported data
    imported_text.config(state=tk.NORMAL)  # Enable text widget for editing
    imported_text.delete(1.0, tk.END)
    imported_text.insert(tk.END, imported_data)
    imported_text.config(state=tk.DISABLED)  # Disable text widget for read-only




