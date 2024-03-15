User Data Web Application Documentation
This documentation provides an overview of a simple web application that allows users to input data, validate it, store it in a database, retrieve it, and display it in a tabular format.

Table of Contents
Introduction
Requirements
Setup
Usage
Folder Structure
Database Schema
Git Repository
Introduction
The User Data Web Application is built using Flask, a micro web framework for Python. It provides a user-friendly interface for users to input their information, including name, email, age, and date of birth. The application performs client-side validation to ensure data integrity and stores the validated data in a SQLite database. Users can also retrieve and view the stored data in a tabular format.

Requirements
To run the User Data Web Application, you need the following software installed:

Python (version >= 3.6)
Flask
SQLite
Setup
Clone the Repository: Clone the repository from your Git hosting platform:

git clone <repository_url>
cd <repository_name>
Install Dependencies: Install Flask using pip:

pip install Flask
Run the Application: Start the Flask application:

python app.py
Access the Application: Open your web browser and navigate to http://localhost:5000 to access the application.

Usage
To use the User Data Web Application:

Fill in the user data form with the required information:
Name
Email
Age
Date of Birth
Click on the "Submit" button.

If the input data is valid, it will be stored in the database.
The stored data can be viewed on the "User Data" page in a tabular format.

Folder Structure
The folder structure of the User Data Web Application is as follows:

app.py: Main Flask application file.
index.html: HTML file for the user data form.
data.html: HTML file to display retrieved user data.
styles.css: CSS file for styling.
scripts.js: JavaScript file for form submission handling.
user_data.db: SQLite database file to store user data.
README.md: Documentation.

Database Schema
The SQLite database schema for storing user data is as follows:

sql

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    dob DATE NOT NULL
);
