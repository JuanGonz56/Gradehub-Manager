import tkinter as tk
from tkinter import messagebox
import csv
import sys
import subprocess

def save_data_to_csv():
    global student_data
    
    # Specify the CSV file path
    csv_file_path = 'Student_data.csv'
    
    # Write the data to the CSV file in write mode (not append)
    with open(csv_file_path, mode='a', newline='') as csvfile:
        fieldnames = ['SID', 'FirstName', 'LastName', 'Email', 'HW1', 'HW2', 'HW3',
                      'Quiz1', 'Quiz2', 'Quiz3', 'Quiz4', 'MidtermExam', 'FinalExam']
        
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
         # If the file is empty, write the header row
    if csvfile.tell() == 0:
        writer.writeheader()

        # Write the data for the new student to the CSV file
    for student in student_data:
        writer.writerow(student)

def export_data_to_csv():
    try:
        # Specify the new CSV file path
        new_csv_file_path = 'New_Student_data.csv'
        
        # Check if the file already exists
        file_exists = True
        with open(new_csv_file_path, 'w', newline='') as new_csv_file:
            if new_csv_file.tell() == 0:
                file_exists = False
        
        # Open the current CSV file for reading
        with open('Student_data.csv', 'r', newline='') as current_csv_file:
            csv_reader = csv.reader(current_csv_file)
            
            # Open the new CSV file for writing, append if it exists
            with open(new_csv_file_path, 'a', newline='') as new_csv_file:
                csv_writer = csv.writer(new_csv_file)
                
                # If the new file is empty, write the header row
                if not file_exists:
                    header_row = next(csv_reader)
                    csv_writer.writerow(header_row)
                
                # Write the data rows
                for row in csv_reader:
                    csv_writer.writerow(row)
    
        # Display a success message
        messagebox.showinfo("Success", f"Data exported to {new_csv_file_path}")
    
        # Open the exported CSV file using the default viewer
        if sys.platform.startswith('win'):
            subprocess.run(['start', new_csv_file_path], shell=True)
        else:
            subprocess.run(['open', new_csv_file_path])
    except Exception as e:
        # Handle any exceptions that might occur during export
        messagebox.showerror("Error", f"Error exporting data: {str(e)}")