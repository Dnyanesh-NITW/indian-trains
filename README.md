# indian-trains

## Intoduction

Welcome to the Indian Trains Database Management System Mini project! This project aims to provide a simple web application for managing a database of train information, including searching for trains, adding new trains, and displaying train schedules.

**Project Status**: This project is currently under development and will be updated soon. Feel free to explore the existing features and codebase. Please note that some functionalities may be incomplete or will be changed in future updates.

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- HTML
- CSS
- JavaScript

## Getting Started

### Prerequisites

- Python 3.x
- XAMPP or any other compatible web server with Apache and MySQL

### Installation

1. Clone the repository
2. Start Apache and MySQL services in XAMPP.
3. Create a MySQL database:
   - Open phpMyAdmin or any MySQL client tool.
   - Create a new database named 'irctc' and import the sql file given in the repository
4. Open the project folder in your preferred IDE (e.g., VS Code).
5. Install the required Python packages
6. Configure the database connection:
   - Open main.py in a text editor.
   - Update the database connection URI in the app.config['SQLALCHEMY_DATABASE_URI'] line:
        ``app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/irctc'``
     Replace 'username' and 'password' with your MySQL credentials. If you are using the default XAMPP configuration, the username is ' 
     'root', and there is no password (leave it empty).
7. Run the application
8. Open your web browser and visit http://localhost:5000 to access the application.


### Features

- Search for trains based on source and destination stations.
- Add new trains to the database.
- Display train schedules.

  


