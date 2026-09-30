# 🏥 Patient Record Management System

## 📌 Project Description

Patient Record Management System is a simple web-based application developed using **Python Flask, HTML, CSS, and SQLite**. It helps users manage patient information digitally. Users can add, view, and edit patient records through a simple web interface.

This project is developed as a beginner-friendly **Full Stack Web Development** project using VS Code.

---

## 🎯 Objectives

- To store patient information digitally.
- To add new patient records.
- To view existing patient records.
- To edit patient information.
- To use SQLite for database storage.
- To understand frontend and backend integration.
- To learn Python Flask web development.

---

## 🛠️ Technologies Used

- **Frontend:** HTML, CSS
- **Backend:** Python, Flask
- **Database:** SQLite
- **IDE:** Visual Studio Code
- **Version Control:** Git and GitHub

---

## ✨ Features

- Add Patient
- View Patient Records
- Edit Patient Records
- Store data using SQLite
- Simple and user-friendly interface
- Flask-based backend
- HTML/CSS frontend
- Local database storage

---

## 📂 Project Structure

    patient record management/
    │
    ├── app.py
    ├── requirements.txt
    ├── README.md
    ├── .gitignore
    ├── patients.db
    │
    ├── templates/
    │   ├── index.html
    │   ├── add_patient.html
    │   └── edit_patient.html
    │
    └── static/
        └── style.css

---

## 📄 File Description

### app.py

This is the main Flask backend file. It handles:

- Flask application
- Database connection
- Creating the patient table
- Adding patients
- Viewing patients
- Editing patients

### index.html

Displays all patient records in a table.

### add_patient.html

Provides a form to add a new patient.

### edit_patient.html

Provides a form to edit existing patient information.

### style.css

Contains the CSS used to design and style the application.

### requirements.txt

Contains the required Python package:

    Flask

### patients.db

SQLite database used to store patient records.

---

## 🗄️ Database Structure

The project uses an SQLite database named:

    patients.db

The database contains a table named:

    patients

The table contains:

| Column | Description |
|---|---|
| id | Unique patient ID |
| name | Patient name |
| age | Patient age |
| gender | Patient gender |
| phone | Patient phone number |
| disease | Patient disease |

---

## 🔄 Application Workflow

    User
      ↓
    Web Browser
      ↓
    HTML + CSS
      ↓
    Flask Backend
      ↓
    SQLite Database
      ↓
    Patient Records

---

## 🔗 Flask Routes

| Route | Method | Purpose |
|---|---|---|
| `/` | GET | View patient records |
| `/add` | GET, POST | Add patient |
| `/edit/<id>` | GET, POST | Edit patient |
| `/delete/<id>` | GET | Delete patient |

The Delete option is not displayed in the current user interface.

---

## ⚙️ Installation

### Step 1: Install Python

Install Python on your computer.

Check Python:

    python --version

---

### Step 2: Open Project in VS Code

Open the project folder:

    patient record management

---

### Step 3: Open Terminal

In VS Code:

    Terminal → New Terminal

### Step 4: Go to Project Folder

    cd "C:\Users\ummak\OneDrive\Desktop\patient record management"

### Step 5: Install Flask

    python -m pip install flask

### Step 6: Install Requirements

    python -m pip install -r requirements.txt
## ▶️ Run the Application

Run:

    python app.py

The Flask server will start.

Open the browser and visit:

    http://127.0.0.1:5000

## ➕ Add Patient

Click:

    Add Patient

Enter:

- Patient Name
- Age
- Gender
- Phone
- Disease

Then click:

    Add Patient

The patient information will be stored in the SQLite database

## 👁️ View Patient

The home page displays patient records in a table.

The table contains:

- ID
- Name
- Age
- Gender
- Phone
- Disease
- Edit

---

## ✏️ Edit Patient

Click the:

    Edit

button for a patient.

Change the required information and click:

    Update Patient

The database will be updated
## 🧪 Example
Example patient record:
    ID: 1
    Name: Lakshmi
    Age: 27
    Gender: Female
    Phone: 9966853308
    Disease: Fever
## 🔐 Security and Privacy
Patient information is sensitive. This project is intended for educational purposes only.
A real healthcare application should include:
- User authentication
- Password protection
- Role-based access
- HTTPS
- Database encryption
- Secure backups
- Input validation
- Access control
- Data privacy protection

Do not upload real patient information to a public GitHub repository.
## ☁️ Cloud Computing Extension

This project can be converted into a cloud-based application.

Cloud architecture:

    User
      ↓
    Web Browser
      ↓
    Cloud Hosting
      ↓
    Flask Application
      ↓
    Cloud Database
      ↓
    Patient Records

Possible cloud platforms:

- Amazon Web Services (AWS)
- Microsoft Azure
- Google Cloud

The Flask application can be deployed to a cloud server and the database can be hosted using a cloud database service.

## 🚀 Future Enhancements

Future versions can include:

- Login and registration
- Doctor login
- Admin dashboard
- Patient search
- Appointment management
- Prescription management
- Medical report upload
- Patient history
- Dashboard and statistics
- Email notifications
- MySQL database
- PostgreSQL database
- Cloud deployment
- Mobile responsive design
- Better security

## 📚 Learning Outcomes

This project helps students understand:

- Python
- Flask
- HTML
- CSS
- SQLite
- CRUD operations
- Database connectivity
- Frontend development
- Backend development
- Full Stack development
- Git
- GitHub
- Basic cloud deployment

## 🧪 Testing

| Test | Result |
|---|---|
| Start Flask application | ✅ Passed |
| Open home page | ✅ Passed |
| Add patient | ✅ Passed |
| View patient | ✅ Passed |
| Edit patient | ✅ Passed |
| Store data in SQLite | ✅ Passed |

## 📸 Screenshots

You can add screenshots of:

1. Home Page
2. Add Patient Page
3. Edit Patient Page

Example:

    screenshots/
    ├── home.png
    ├── add-patient.png
    └── edit-patient.png

## 👩‍💻 Author

**Poojitha**

## 📜 License

This project is created for educational purposes.

It can be used and modified for learning and academic projects.

## ⭐ Conclusion

The Patient Record Management System is a beginner-friendly full-stack web application developed using Python Flask, HTML, CSS, and SQLite. It provides basic patient record management features such as adding, viewing, and editing patient information. The project demonstrates how frontend, backend, and database technologies work together to create a web application.


## 🔒 .gitignore

The following files should not be uploaded to GitHub:

    patients.db
    __pycache__/
    *.pyc

This is especially important because the database may contain patient information.

Project Status

**Status: Completed ✅**

The basic Patient Record Management System is working with:

- Frontend ✅
- Backend ✅
- Database ✅
- Add Patient ✅
- View Patient ✅
- Edit Patient ✅
- GitHub Ready ✅
