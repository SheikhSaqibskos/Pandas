📊 Pandas – Student Management System
Class Work & Assignment – Pandas

Al-Khair Institute of Technology

Assignment No: 5 — Pandas Basics

Prepared By: Sheikh Saqib

📘 Project Overview

This repository contains a complete Student Management System built using Python and Pandas.
It demonstrates practical usage of pandas for:

Creating and modifying DataFrames

Updating student records

Calculating results (Total, Percentage, Grade)

Performing CRUD operations using a menu-driven system

This assignment reflects essential pandas operations suitable for beginners and intermediate learners working with tabular data.

🧾 Features of the Student Management System
✅ 1. Create DataFrame

Starts with a DataFrame of 10 students and their marks in:

Python

Excel

Power BI

Pandas

Machine Learning

Statistics

Includes name and roll number for each student.

✅ 2. Calculate Results

A custom function computes:

Total Marks

Percentage

Grade using conditions:

A+ → 90% and above

A → 80–89%

B → 70–79%

C → 60–69%

D → below 60%

This demonstrates DataFrame column operations, conditional logic, and vectorized calculations.

✅ 3. Add New Student

Allows user input to add new rows dynamically.
Covers:

Reading input

Creating dictionary-based new rows

Appending into DataFrame using .loc[]

✅ 4. Remove Student

Removes a record based on Roll No using filtering:

df = df[df['roll No'] != roll]


Shows DataFrame row deletion techniques.

✅ 5. Modify Student Marks

Lets the user:

Search student by roll number

Update marks for a specific subject

Replace values using .loc[]

Useful for understanding record editing in DataFrames.

✅ 6. Menu System

A complete interactive CLI program with options:

1. Show DataFrame  
2. Add Student  
3. Remove Student  
4. Modify Student  
5. Calculate Results  
6. Exit  


Makes the project function like a small management software.

🛠️ Technologies Used

Python 3.x

Pandas Library

Install pandas using:

pip install pandas

🚀 How to Run the Program

Clone the repository:

git clone https://github.com/sheikhsaqibskos/Pandas.git


Open the project in any IDE (VS Code, PyCharm, Jupyter, etc.)

Run the script:

python main.py


Follow the menu instructions.

📂 Files Included

student_management.py or .ipynb — Main code file

README.md — Project documentation (this file)

🎯 Learning Outcomes

Through this assignment, you will understand:

DataFrame creation & manipulation

CRUD operations in pandas

Column-wise calculations

Conditional grading logic

CLI-based interactive applications

Real-world usage of pandas for data handling

📜 License

This project is for educational purposes and may be reused with proper credit.
