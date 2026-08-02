from flask import Flask, render_template, request, redirect
from database import connect_db

app = Flask(__name__)


# 1. HOME (Add Student Form)
@app.route("/")
def home():
    return render_template("index.html")


# 2. CREATE (Add Student)
@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    age = request.form["age"]
    department = request.form["department"]
    email = request.form["email"]

    connection = connect_db()
    cursor = connection.cursor()

    sql = """
    INSERT INTO students (name, age, department, email)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(sql, (name, age, department, email))
    connection.commit()

    cursor.close()
    connection.close()

    return redirect("/students")


# 3. READ & SEARCH (View Students)
@app.route("/students")
def students():
    search_query = request.args.get("search", "").strip()

    connection = connect_db()
    cursor = connection.cursor()

    if search_query:
        sql = """
        SELECT * FROM students 
        WHERE name LIKE %s OR email LIKE %s OR department LIKE %s
        """
        wildcard = f"%{search_query}%"
        cursor.execute(sql, (wildcard, wildcard, wildcard))
    else:
        cursor.execute("SELECT * FROM students")

    students_data = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("view_students.html", students=students_data, search_query=search_query)


# 4. EDIT PAGE (Fetch Student by ID)
@app.route("/edit/<int:id>")
def edit(id):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students WHERE id=%s", (id,))
    student = cursor.fetchone()

    cursor.close()
    connection.close()

    return render_template("edit_student.html", student=student)


# 5. UPDATE (Save edited details to DB)
@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    name = request.form["name"]
    age = request.form["age"]
    department = request.form["department"]
    email = request.form["email"]

    connection = connect_db()
    cursor = connection.cursor()

    sql = """
    UPDATE students
    SET name=%s, age=%s, department=%s, email=%s
    WHERE id=%s
    """

    cursor.execute(sql, (name, age, department, email, id))
    connection.commit()

    cursor.close()
    connection.close()

    return redirect("/students")


# 6. DELETE (Remove student from DB)
@app.route("/delete/<int:id>")
def delete(id):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    connection.commit()

    cursor.close()
    connection.close()

    return redirect("/students")


if __name__ == "__main__":
    app.run(debug=True)