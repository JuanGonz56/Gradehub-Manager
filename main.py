import tkinter as tk
from tkinter import ttk
from import_data import import_data
from add_delete_student import add_student, delete_student
from search_student import search_student
from update_scores import update_scores
from average_scores import search_task_scores
from export_data_to_csv import export_data_to_csv
from tkinter.filedialog import askopenfile


# Define global variables to store and manipulate data
student_data = []
imported_data = ""  # Store the imported data

# Create the main window
root = tk.Tk()
root.title("Gradebook System")

# Create a notebook to organize different functionalities
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Create tabs for each functionality
import_tab = ttk.Frame(notebook)
add_delete_tab = ttk.Frame(notebook)
search_tab = ttk.Frame(notebook)
update_tab = ttk.Frame(notebook)
average_scores_tab = ttk.Frame(notebook)
export_tab = ttk.Frame(notebook)

notebook.add(import_tab, text="Import Data")
notebook.add(add_delete_tab, text="Add/Delete Student")
notebook.add(search_tab, text="Search Student")
notebook.add(update_tab, text="Update Scores")
notebook.add(average_scores_tab, text="Average Scores")
notebook.add(export_tab, text="Export Data")

# Average scores Tab
task_name_label = tk.Label(average_scores_tab, text="Search Assignment:")
task_name_entry = tk.Entry(average_scores_tab)

# Place labels, input fields, and buttons in the average scores tab
task_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
task_name_entry.grid(row=1, column=2, padx=5, pady=5)

# Create a text box to display the average data
average_text = tk.Text(average_scores_tab, height=20, width=50)
average_text.grid(padx=20, pady=0)

# Create a button to trigger the search
search_button = tk.Button(average_scores_tab, text="Search", command=search_task_scores)
search_button.grid(row=1, column=3, padx=5, pady=5)


# Add Student Tab
sid_label = tk.Label(add_delete_tab, text="SID to Add:")
sid_entry = tk.Entry(add_delete_tab)

first_name_label = tk.Label(add_delete_tab, text="FirstName:")
first_name_entry = tk.Entry(add_delete_tab)

last_name_label = tk.Label(add_delete_tab, text="LastName:")
last_name_entry = tk.Entry(add_delete_tab)

email_label = tk.Label(add_delete_tab, text="Email:")
email_entry = tk.Entry(add_delete_tab)

add_student_button = tk.Button(add_delete_tab, text="Add Student", command=add_student)

# Place labels, input fields, and buttons in the Add Student Tab
sid_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
sid_entry.grid(row=1, column=1, padx=5, pady=5)

first_name_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
first_name_entry.grid(row=2, column=1, padx=5, pady=5)

last_name_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
last_name_entry.grid(row=3, column=1, padx=5, pady=5)

email_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
email_entry.grid(row=4, column=1, padx=5, pady=5)

add_student_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

# Delete Student Tab
delete_sid_label = tk.Label(add_delete_tab, text="SID to Delete:")
delete_sid_entry = tk.Entry(add_delete_tab)
delete_student_button = tk.Button(add_delete_tab, text="Delete Student", command=delete_student)


# Delete Student Tab
delete_sid_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
delete_sid_entry.grid(row=0, column=1, padx=10, pady=5)
delete_student_button.grid(row=0, column=2, columnspan=2, padx=5, pady=10)

# Import Data Tab
import_data_button = tk.Button(import_tab, text="Import Data", command=import_data)
import_data_button.pack(padx=20, pady=50)

# Create a text box to display the imported data
imported_text = tk.Text(import_tab, height=20, width=60)
imported_text.pack(padx=20, pady=10)

# Optionally, you can add a label to indicate the import status
import_status_label = tk.Label(import_tab, text="")
import_status_label.pack()

# Search Student Tab
search_sid_label = tk.Label(search_tab, text="SID to Search:")
search_sid_entry = tk.Entry(search_tab)
search_student_button = tk.Button(search_tab, text="Search Student", command=search_student)
result_label = tk.Label(search_tab, text="")

# Create a text box to display the searched student
searched_student_text = tk.Text(search_tab, height=10, width=50)
searched_student_text.grid(row=3, column=0, columnspan=2, padx=20, pady=10)

# Place labels, input fields, and buttons in the Search Student Tab
search_sid_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
search_sid_entry.grid(row=0, column=1, padx=5, pady=5)
search_student_button.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
result_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

# Update Scores Tab
update_sid_label = tk.Label(update_tab, text="SID to Update:")
update_sid_entry = tk.Entry(update_tab)

update_hw1_label = tk.Label(update_tab, text="New HW1 Score:")
update_hw1_entry = tk.Entry(update_tab)

update_hw2_label = tk.Label(update_tab, text="New HW2 Score:")
update_hw2_entry = tk.Entry(update_tab)

update_hw3_label = tk.Label(update_tab, text="New HW3 Score:")
update_hw3_entry = tk.Entry(update_tab)

update_quiz1_label = tk.Label(update_tab, text="New Quiz 1 Score:")
update_quiz1_entry = tk.Entry(update_tab)

update_quiz2_label = tk.Label(update_tab, text="New Quiz 2 Score:")
update_quiz2_entry = tk.Entry(update_tab)

update_quiz3_label = tk.Label(update_tab, text="New Quiz 3 Score:")
update_quiz3_entry = tk.Entry(update_tab)

update_quiz4_label = tk.Label(update_tab, text="New Quiz 4 Score:")
update_quiz4_entry = tk.Entry(update_tab)

update_midterm_label = tk.Label(update_tab, text="New Midterm Score:")
update_midterm_entry = tk.Entry(update_tab)

update_final_label = tk.Label(update_tab, text="New Final Score:")
update_final_entry = tk.Entry(update_tab)

update_scores_button = tk.Button(update_tab, text="Update Scores", command=update_scores)


# Place labels, input fields, and buttons in the Update Scores Tab
update_sid_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
update_sid_entry.grid(row=0, column=1, padx=5, pady=5)

update_hw1_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
update_hw1_entry.grid(row=1, column=1, padx=5, pady=5)

update_hw2_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
update_hw2_entry.grid(row=2, column=1, padx=5, pady=5)

update_hw3_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
update_hw3_entry.grid(row=3, column=1, padx=5, pady=5)


update_quiz1_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
update_quiz1_entry.grid(row=4, column=1, padx=5, pady=5)

update_quiz2_label.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
update_quiz2_entry.grid(row=5, column=1, padx=5, pady=5)

update_quiz3_label.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)
update_quiz3_entry.grid(row=6, column=1, padx=5, pady=5)

update_quiz4_label.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)
update_quiz4_entry.grid(row=7, column=1, padx=5, pady=5)

update_midterm_label.grid(row=8, column=0, padx=5, pady=5, sticky=tk.W)
update_midterm_entry.grid(row=8, column=1, padx=5, pady=5)

update_final_label.grid(row=9, column=0, padx=5, pady=5, sticky=tk.W)
update_final_entry.grid(row=9, column=1, padx=5, pady=5)

update_scores_button.grid(row=10, column=0, columnspan=2, padx=5, pady=10)

# Create a button to trigger the export
export_data_button = tk.Button(export_tab, text="Export Data", command=export_data_to_csv)
export_data_button.grid(padx=20, pady=10)

# Create a label to display the export result
export_result_label = tk.Label(export_tab, text="")
export_result_label.grid(padx=20, pady=10)

# Create the main window
root.mainloop()
