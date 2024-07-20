# Todo App

## Table of Contents
- [Todo App](#todo-app)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Tech Stack](#tech-stack)
    - [Backend](#backend)
    - [Frontend](#frontend)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
      - [Backend (FastAPI)](#backend-fastapi)
      - [Frontend (Flutter)](#frontend-flutter)
    - [Running the Application](#running-the-application)
  - [API Endpoints](#api-endpoints)
    - [Authentication](#authentication)
    - [Tasks](#tasks)
  - [Project Structure](#project-structure)
    - [Backend (FastAPI)](#backend-fastapi-1)
    - [Frontend (Flutter)](#frontend-flutter-1)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

## Introduction
The Todo App is a simple yet powerful task management application developed using FastAPI for the backend and Flutter for the frontend. This application allows users to add, edit, delete, and view tasks, helping them manage their day-to-day activities efficiently.

## Features
- User authentication and authorization
- Create, read, update, and delete tasks
- Mark tasks as completed
- Filter tasks based on status (completed, pending)
- Responsive UI with Flutter

## Tech Stack
### Backend
- **Framework:** FastAPI
- **Database:** SQLite (or any preferred database)
- **Authentication:** JWT (JSON Web Tokens)

### Frontend
- **Framework:** Flutter
- **State Management:** Bloc (Business Logic Component)

## Getting Started

### Prerequisites
- Python 3.12+
- Flutter 3.18+

### Installation

#### Backend (FastAPI)
1. Clone the repository:
    ```
    git clone https://github.com/yourusername/todo-app.git
    cd todo-app/backend
    ```

2. Create a virtual environment and activate it:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```
    python main.py create_db
    ```

5. Run the FastAPI server:
    ```
    uvicorn main:app --reload
    ```

#### Frontend (Flutter)
1. Navigate to the frontend directory:
    ```
    cd ../frontend
    ```

2. Install the dependencies:
    ```
    flutter pub get
    ```

3. Run the Flutter app:
    ```
    flutter run
    ```

### Running the Application
- Start the FastAPI server:
    ```
    uvicorn main:app --reload
    ```
- Run the Flutter app:
    ```
    flutter run
    ```

## API Endpoints
### Authentication
- **POST** `/auth/register` - Register a new user
- **POST** `/auth/login` - Login and get a JWT token

### Tasks
- **GET** `/tasks` - Get all tasks
- **POST** `/tasks` - Create a new task
- **GET** `/tasks/{task_id}` - Get a task by ID
- **PUT** `/tasks/{task_id}` - Update a task by ID
- **DELETE** `/tasks/{task_id}` - Delete a task by ID

## Project Structure
### Backend (FastAPI)
```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── auth.py
│   └── database.py
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   └── test_tasks.py
├── requirements.txt
└── README.md
```

### Frontend (Flutter)
```
frontend/
├── lib/
│   ├── main.dart
│   ├── models/
│   ├── screens/
│   ├── blocs/
│   ├── events/
│   ├── states/
│   ├── services/
│   ├── widgets/
├── test/
├── pubspec.yaml
└── README.md
```

## Contributing
Contributions are welcome! Please follow the steps below to contribute:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
- **Email:** bobur.yu@anur.tech
- **GitHub:** [dev-yusupov](https://github.com/dev-yusupov)

---

Feel free to customize this template further according to your project's specific details and requirements.