To-Do List Application
Description

A simple command-line To-Do List application developed using Python. It allows users to manage their daily tasks by adding, viewing, completing, and deleting tasks.

The application uses a JSON file (tasks.json) to store tasks permanently, so tasks are available even after closing the program.

Features
Add Task: Add new tasks to your to-do list.
View Tasks: Display all tasks and their completion status.
Mark Task as Done: Mark a task as completed.
Delete Task: Remove tasks from the list.
Data Persistence: Save and load tasks using a JSON file.
Input Validation: Prevent empty tasks and handle invalid inputs.
Technologies Used
Python 3
JSON
Pytest (for testing)
Project Structure
text
todo-list/
│
├── todo.py
├── test_todo.py
├── tasks.json
├── requirements.txt
└── README.md

Installation
Clone or download this project.
Open the project folder in your terminal.
Install the required dependencies:
bash
pip install -r requirements.txt

How to Run

Run the application using:

bash
python todo.py

Application Menu
text
--- TO-DO LIST ---
1. Add Task
2. View Task
3. Mark Task as done
4. Delete Task
5. Exit


Choose an option from 1 to 5 to manage your tasks.

Running Tests

This project uses Pytest for unit testing.

Run all tests using:

bash
pytest -v


The tests cover:

Adding tasks
Adding empty tasks
Viewing tasks
Marking tasks as completed
Deleting tasks
Handling invalid inputs
Saving and loading tasks
Handling missing JSON files
Data Storage

Tasks are stored in a file called tasks.json in JSON format.

Example:

json
[
    {
        "task": "Study Python",
        "done": false
    },
    {
        "task": "Complete project",
        "done": true
    }
]

Future Improvements
Add task deadlines.
Add task priorities.
Search for tasks.
Add a graphical user interface (GUI).
Filter completed and pending tasks.
Author

Developed as a Python programming project.