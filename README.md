# 🎓 Student Management System

A clean, responsive, full-stack web application built with **Python**, **Flask**, and **MySQL**. This application allows administrators to easily manage student records through complete **CRUD** (Create, Read, Update, Delete) operations and real-time search/filter capabilities.

---

## ✨ Features

- ➕ **Create:** Add new students with Name, Age, Department, and Email details.
- 📋 **Read:** View a formatted, responsive table of all registered students.
- ✏️ **Update:** Dynamically fetch and update existing student records by ID.
- 🗑️ **Delete:** Permanently remove records with client-side confirmation prompts.
- 🔍 **Search & Filter:** Instantly filter students by Name, Email, or Department using dynamic SQL queries.

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Database:** MySQL (using parameterized queries for SQL injection prevention)
- **Frontend:** HTML5, CSS3, Jinja2 Templating
- **Version Control:** Git, GitHub

---

## 📁 Project Structure

```text
Student-Management-System/
│
├── app.py              # Main Flask server and route logic
├── database.py         # MySQL connection helper configuration
│
├── templates/          # Jinja2 HTML templates
│   ├── index.html          # Add Student form page
│   ├── view_students.html  # Student table & search view
│   └── edit_student.html  # Edit Student form page
│
└── static/             # Static assets
    └── style.css           # Custom CSS styles
