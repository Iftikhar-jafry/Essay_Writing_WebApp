# ✍️ Essay Writing Web App

A responsive web application built using **Flask** and **Bootstrap** that allows users to write essays, save them in a database, update or delete entries, and view saved content. The app uses **Jinja2 templating** for dynamic rendering and **SQLAlchemy** as the ORM to handle database operations.

---

## 🚀 Features

- 📝 Write essays with a title and rich textarea
- 💾 Save essays into a SQLite database
- 📖 Read saved essays in a styled layout
- ✏️ Update existing essays
- 🗑️ Delete essays
- ✅ Responsive UI using **Bootstrap 5**
- ⚙️ Dynamic rendering with **Jinja2 templates**

---

## 🛠️ Tech Stack

| Technology     | Purpose                         |
|----------------|----------------------------------|
| **HTML/CSS**   | Structure and styling            |
| **Bootstrap 5**| Responsive, modern UI components |
| **Flask**      | Web backend framework            |
| **Jinja2**     | Dynamic HTML rendering           |
| **SQLAlchemy** | ORM for database operations      |
| **SQLite**     | Local lightweight database       |
| **VS Code**    | Code editor                      |

---

## 🗂️ Project Structure

Essay_Writing_WebApp/
│
├── templates/
│ ├── index.html # Main writing form
│ └── read.html # Display saved essays
│
├── Writing_Essay.db # SQLite database file
├── app.py # Flask application logic
├── static/ # (Optional) CSS/JS if added
└── README.md # Project documentation


---

## ⚙️ Setup Instructions

### 1. 📦 Clone the repository

git clone https://github.com/your-username/essay-writing-app.git
cd essay-writing-app

python -m venv .venv
source .venv/bin/activate     # On Linux/macOS
.venv\Scripts\activate        # On Windows

pip install flask flask_sqlalchemy

## 💡 Usage Guide
- Write & Submit: Go to the homepage, write a title and essay content, and click "Submit".

- Read: Click on the Read Mode button to view saved essays.

- Edit/Delete: Use the buttons below each essay card in the Read section.


## 📸 Screenshots
