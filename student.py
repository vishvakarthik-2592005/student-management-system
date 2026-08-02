from database import connect_db


def add_student():
    connection = connect_db()
    cursor = connection.cursor()

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")
    email = input("Enter Email: ")

    sql = """
    INSERT INTO students (name, age, department, email)
    VALUES (%s, %s, %s, %s)
    """

    values = (name, age, department, email)

    cursor.execute(sql, values)
    connection.commit()

    print("\nStudent Added Successfully!\n")

    cursor.close()
    connection.close()


def view_students():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    print("\n========== Student List ==========")

    if len(students) == 0:
        print("No students found.")
    else:
        for student in students:
            print(f"ID         : {student[0]}")
            print(f"Name       : {student[1]}")
            print(f"Age        : {student[2]}")
            print(f"Department : {student[3]}")
            print(f"Email      : {student[4]}")
            print("-" * 35)

    cursor.close()
    connection.close()


def update_student():
    connection = connect_db()
    cursor = connection.cursor()

    student_id = int(input("Enter Student ID to update: "))

    new_name = input("Enter New Name: ")
    new_age = int(input("Enter New Age: "))
    new_department = input("Enter New Department: ")
    new_email = input("Enter New Email: ")

    sql = """
    UPDATE students
    SET name=%s, age=%s, department=%s, email=%s
    WHERE id=%s
    """

    values = (
        new_name,
        new_age,
        new_department,
        new_email,
        student_id
    )

    cursor.execute(sql, values)
    connection.commit()

    if cursor.rowcount > 0:
        print("\nStudent Updated Successfully!\n")
    else:
        print("\nStudent ID not found.\n")

    cursor.close()
    connection.close()


def delete_student():
    connection = connect_db()
    cursor = connection.cursor()

    student_id = int(input("Enter Student ID to delete: "))

    sql = "DELETE FROM students WHERE id = %s"

    cursor.execute(sql, (student_id,))
    connection.commit()

    if cursor.rowcount > 0:
        print("\nStudent Deleted Successfully!\n")
    else:
        print("\nStudent ID not found.\n")

    cursor.close()
    connection.close()


def search_student():
    connection = connect_db()
    cursor = connection.cursor()

    name = input("Enter Student Name: ")

    sql = "SELECT * FROM students WHERE name = %s"

    cursor.execute(sql, (name,))

    students = cursor.fetchall()

    if len(students) == 0:
        print("\nStudent not found.\n")
    else:
        print("\n===== Search Result =====")
        for student in students:
            print(f"ID         : {student[0]}")
            print(f"Name       : {student[1]}")
            print(f"Age        : {student[2]}")
            print(f"Department : {student[3]}")
            print(f"Email      : {student[4]}")
            print("-" * 35)

    cursor.close()
    connection.close()