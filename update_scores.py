import tkinter as tk
from tkinter import messagebox
import csv

def update_scores():
    # Retrieve input values (SID and scores) from the user
    sid = int(update_sid_entry.get())
    hw1 = int(update_hw1_entry.get())
    hw2 = int(update_hw2_entry.get())
    hw3 = int(update_hw3_entry.get())
    quiz1 = int(update_quiz1_entry.get())
    quiz2 = int(update_quiz2_entry.get())
    quiz3 = int(update_quiz3_entry.get())
    quiz4 = int(update_quiz4_entry.get())
    midterm = int(update_midterm_entry.get())
    final = int(update_final_entry.get())
    
    # Call the update_scores_data function with user inputs
    update_scores_data(sid, hw1, hw2, hw3, quiz1, quiz2, quiz3, quiz4, midterm, final)



def update_scores_data(sid, hw1, hw2, hw3, quiz1, quiz2, quiz3, quiz4, midterm, final):
    # Read the data from the CSV file into a list of dictionaries
    student_data = []
    with open('Student_data.csv', mode='r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            student_data.append(row)
    
    # Initialize a flag to check if the student was found
    student_found = False
    
    # Update the scores for the found student
    for student in student_data:
        if int(student['SID']) == sid:
            student['HW1'] = hw1
            student['HW2'] = hw2
            student['HW3'] = hw3
            student['Quiz1'] = quiz1
            student['Quiz2'] = quiz2
            student['Quiz3'] = quiz3
            student['Quiz4'] = quiz4
            student['MidtermExam'] = midterm
            student['FinalExam'] = final
            student_found = True
    
    if not student_found:
        # If the student is not found, display an error message
        print("Student not found in the CSV file.")
        return

    # Write the updated data back to the CSV file
    with open('Student_data.csv', mode='w', newline='') as csvfile:
        fieldnames = student_data[0].keys()
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(student_data)

# Example usage:
# update_scores_data(35902, 95, 85, 75, 92, 88, 75, 90, 88, 78)


# Function to handle the search button click event
def search_task_scores():
    task_name = task_name_entry.get()

    # Initialize lists to store scores for the selected task
    scores = []

    # Open the CSV file and read data
    with open('Student_data.csv', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            if task_name in row and row[task_name].strip():  # Check if task exists and is not empty
                scores.append(float(row[task_name]))

    if not scores:
        average_text.delete(1.0, tk.END)
        average_text.insert(tk.END, f"Task '{task_name}' not found or no scores available.")
    else:
        # Calculate maximum, minimum, and mean scores
        max_score = max(scores)
        min_score = min(scores)
        mean_score = sum(scores) / len(scores)

        # Display the results in the Text widget
        average_text.delete(1.0, tk.END)
        average_text.insert(tk.END, f"Assignment: {task_name}\n")
        average_text.insert(tk.END, f"Maximum: {max_score}\n")
        average_text.insert(tk.END, f"Minimum: {min_score}\n")
        average_text.insert(tk.END, f"Mean: {mean_score:.2f}\n")