import tkinter as tk
from tkinter import messagebox
import csv

def add_student():
    sid = int(sid_entry.get())
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    email = email_entry.get()

    # Call the add_student_data function to add the student to the CSV file
    add_student_data(sid, first_name, last_name, email)

    # Optionally, clear the input fields after adding the student
    sid_entry.delete(0, tk.END)
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)


def add_student_data(sid, first_name, last_name, email):
    # Load existing CSV data into a DataFrame
    csv_file_path = 'Student_data.csv'
    df = pd.read_csv(csv_file_path)

    # Check if the student with the given SID already exists
    existing_student = df[df['SID'] == sid]

    if not existing_student.empty:
        # Update the student's information if they already exist
        df.loc[df['SID'] == sid, 'FirstName'] = first_name
        df.loc[df['SID'] == sid, 'LastName'] = last_name
        df.loc[df['SID'] == sid, 'Email'] = email
    else:
        # Add a new student if they don't exist
        new_student = {
            'SID': sid,
            'FirstName': first_name,
            'LastName': last_name,
            'Email': email,
            'HW1': None,
            'HW2': None,
            'HW3': None,
            'Quiz1': None,
            'Quiz2': None,
            'Quiz3': None,
            'Quiz4': None,
            'MidtermExam': None,
            'FinalExam': None,
        }
        new_student_df = pd.DataFrame([new_student])  # Create a new DataFrame

        # Exclude empty or all-NA columns before concatenating
        columns_to_exclude = [col for col in new_student_df.columns if new_student_df[col].count() == 0]
        new_student_df = new_student_df.drop(columns=columns_to_exclude)

        # Concatenate the new student DataFrame with the existing DataFrame
        df = pd.concat([df, new_student_df], ignore_index=True)

    # Write the updated data back to the CSV file
    df.to_csv(csv_file_path, index=False)


def clear_input_fields():
    # Clear input fields
    sid_entry.delete(0, 'end')
    first_name_entry.delete(0, 'end')
    last_name_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    

def delete_student_data(sid_to_delete):
    try:
        sid_to_delete = int(sid_to_delete)

        # Load the CSV file into a list of dictionaries
        csv_file_path = 'Student_data.csv'
        with open(csv_file_path, mode='r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            student_data = list(csv_reader)

        # Check if the SID exists in the student data
        for student in student_data:
            if int(student['SID']) == sid_to_delete:
                # Delete the student from the list
                student_data.remove(student)

                # Write the updated data back to the CSV file
                with open(csv_file_path, mode='w', newline='') as csvfile:
                    fieldnames = student_data[0].keys()
                    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    csv_writer.writeheader()
                    csv_writer.writerows(student_data)

                # Display a success message using messagebox
                messagebox.showinfo("Success", f"Student with SID {sid_to_delete} deleted.")
                return

        # If student is not found, display an error message
        messagebox.showerror("Error", f"Student with SID {sid_to_delete} not found.")
    except ValueError:
        # Handle invalid SID input
        messagebox.showerror("Error", "Invalid SID. Please enter a valid SID.")

           

# Create a function to handle the "Delete Student" button click event
def delete_student():
    sid_to_delete = delete_sid_entry.get()
    delete_student_data(sid_to_delete)
