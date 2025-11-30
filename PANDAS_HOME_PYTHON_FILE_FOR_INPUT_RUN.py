import pandas as pd

# --------------------------------------------------
# 1. Creating starting DataFrame
# --------------------------------------------------

result = {
    'name': ['Alpha','Bravo', 'Charlie','Delta','Echo','Foxtrot','Golf','Hotel','India','Juliet'],
    'roll No': [11,22,33,44,55,66,77,88,99,111],
    'python': [78,67,89,90,91,72,76,89,67,85],
    'excel': [89,87,67,74,78,90,76,78,90,54],
    'power_bi': [45,67,89,87,67,90,65,67,56,90],
    'pandas': [81,85,89,87,41,45,96,56,93,78],
    'machine_learning':[96,95,84,85,82,81,74,75,96,90],
    'statistics':[67,48,45,98,75,71,70,60,90,93]
}

df = pd.DataFrame(result)

# --------------------------------------------------
# 2. Function: Calculate Result (Total, Percentage, Grade)
# --------------------------------------------------

def calculate_result(df):
    subjects = ['python','excel','power_bi','pandas','machine_learning','statistics']

    # total marks
    df['Total'] = df[subjects].sum(axis=1)

    # percentage
    df['Percentage'] = df['Total'] / (len(subjects)*100) * 100

    # Grade using IF ELIF ELSE
    grade = []
    for p in df['Percentage']:
        if p >= 90:
            grade.append("A+")
        elif p >= 80:
            grade.append("A")
        elif p >= 70:
            grade.append("B")
        elif p >= 60:
            grade.append("C")
        else:
            grade.append("D")

    df['Grade'] = grade
    return df

# --------------------------------------------------
# 3. Add New Student
# --------------------------------------------------

def add_student(df):
    print("\n--- Add Student ---")
    name = input("Enter name: ")
    roll = int(input("Enter roll no: "))
    
    python = int(input("Python marks: "))
    excel = int(input("Excel marks: "))
    power_bi = int(input("Power BI marks: "))
    pandas_m = int(input("Pandas marks: "))
    ml = int(input("Machine Learning marks: "))
    stats = int(input("Statistics marks: "))

    new_student = {
        'name': name,
        'roll No': roll,
        'python': python,
        'excel': excel,
        'power_bi': power_bi,
        'pandas': pandas_m,
        'machine_learning': ml,
        'statistics': stats
    }

    df.loc[len(df)] = new_student
    print("Student Added Successfully!\n")
    return df

# --------------------------------------------------
# 4. Remove Student
# --------------------------------------------------

def remove_student(df):
    print("\n--- Remove Student ---")
    roll = int(input("Enter roll number to delete: "))

    df = df[df['roll No'] != roll]
    print("Student Removed!\n")
    return df

# --------------------------------------------------
# 5. Modify Student Marks
# --------------------------------------------------

def modify_student(df):
    print("\n--- Modify Student Marks ---")
    roll = int(input("Enter roll number to modify: "))

    if roll in df['roll No'].values:
        index = df[df['roll No'] == roll].index[0]
        
        print("Existing Record:\n", df.loc[index])

        subject = input("Enter subject to modify: ").lower()
        new_marks = int(input("Enter new marks: "))

        df.loc[index, subject] = new_marks
        print("Record Updated!\n")
    else:
        print("Roll number not found!")
    return df

# --------------------------------------------------
# 6. Menu System
# --------------------------------------------------

while True:
    print("\n===== Student Management System =====")
    print("1. Show DataFrame")
    print("2. Add Student")
    print("3. Remove Student")
    print("4. Modify Student")
    print("5. Calculate Results")
    print("6. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        print(df)

    elif choice == 2:
        df = add_student(df)

    elif choice == 3:
        df = remove_student(df)

    elif choice == 4:
        df = modify_student(df)

    elif choice == 5:
        df = calculate_result(df)
        print("\nResult Calculated Successfully!")
        print(df)

    elif choice == 6:
        print("Exiting...")
        break

    else:
        print("Invalid Input! Try Again.")
