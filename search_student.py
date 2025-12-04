import tkinter as tk
from tkinter import messagebox
import csv

# Function to calculate the grade based on the specified criteria
def calculate_grade(total_score):
    if total_score >= 90:
        return 'A'
    elif 80 <= total_score < 90:
        return 'B'
    elif 70 <= total_score < 80:
        return 'C'
    elif 60 <= total_score < 70:
        return 'D'
    else:
        return 'F'


def search_student():
    sid_to_search = int(search_sid_entry.get())

    # Open the CSV file
    with open('Student_data.csv', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        # Search for the student with the matching SID
        found_student = None
        for student in csv_reader:
            if int(student['SID']) == sid_to_search:
                found_student = student
                break

    if found_student:
        # Extract the data
        sid = found_student['SID']
        first_name = found_student['FirstName']
        last_name = found_student['LastName']
        email = found_student['Email']

        # Extract and convert homework and quiz scores with default value of 0.0 for empty strings
        homeworks = [float(found_student[f'HW{i}']) if found_student[f'HW{i}'] else 0.0 for i in range(1, 4)]
        quizzes = [float(found_student[f'Quiz{i}']) if found_student[f'Quiz{i}'] else 0.0 for i in range(1, 5)]

        # Extract and convert midterm and final exam scores with default value of 0.0 for empty strings
        midterm = float(found_student['MidtermExam']) if found_student['MidtermExam'] else 0.0
        final = float(found_student['FinalExam']) if found_student['FinalExam'] else 0.0

        # Calculate the total score based on the weights
        total_score = (
            (sum(homeworks) / 3) * 0.2 +
            (sum(quizzes) / 4) * 0.2 +
            midterm * 0.3 +
            final * 0.3
        )

        # Calculate the grade
        grade = calculate_grade(total_score)

        # Format the output
        result_text = f"SID: {sid}\n" \
                      f"FirstName: {first_name}\n" \
                      f"LastName: {last_name}\n" \
                      f"Email: {email}\n" \
                      f"Homeworks: {', '.join(map(str, homeworks))}\n" \
                      f"Quizzes: {', '.join(map(str, quizzes))}\n" \
                      f"MidtermExam: {midterm}\n" \
                      f"FinalExam: {final}\n" \
                      f"Grade: {grade}"

        # Display the result in the search_student_text widget
        searched_student_text.delete(1.0, tk.END)  # Clear previous text
        searched_student_text.insert(tk.END, result_text)
    else:
        # Display an error message if student not found
        searched_student_text.delete(1.0, tk.END)
        searched_student_text.insert(tk.END, "Student not found by SID")

def load_data_from_csv():
    global student_data
    student_data = []  # Clear existing data
    csv_file_path = 'Student_data.csv'
    
    try:
        with open(csv_file_path, mode='r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                student_data.append(row)
    except FileNotFoundError:
        print("CSV file not found.")