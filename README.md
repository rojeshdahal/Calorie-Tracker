# 🍎 Django Calorie Tracker

A full-stack, responsive Calorie Tracker application built with Python, Django, and Tailwind CSS. This application allows users to register, log in, and securely track their daily food intake, meal types, and calorie counts via a personalized dashboard.

## 🚀 Features

- **User Authentication System:** Secure registration, login, and logout functionality.
- **User Ownership & Security:** Personalized data isolation ensuring users can only view, edit, or delete their own logs.
- **Complete CRUD Operations:** Create, Read, Update, and Delete food entries.
- **Dynamic Dashboard:** Aggregated metrics calculating total calories consumed.
- **Modern UI:** Clean, responsive interface styled with Tailwind CSS.
- **Form Validation:** Built-in Django forms handling date pickers, dropdown selections, and input validation.

## 🛠️ Tech Stack

- Backend: Python, Django
- Database: SQLite (Default development database)
- Frontend: HTML5, Tailwind CSS (via CDN)
- Authentication: Django Built-in Auth (UserCreationForm, LoginView, LogoutView)

## 📋 Database Architecture

The application uses a One-to-Many relationship between the built-in Django User model and the tracking logs.

## 💻 Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation & Setup

Clone the repository:

```bash
git clone https://github.com/yourusername/calorie-tracker-django.git
cd calorie-tracker-django
```

Create and activate a virtual environment:

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

Install Django:

```bash
pip install django
```

Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create a superuser (for admin panel access):

```bash
python manage.py createsuperuser
```

Run the development server:

```bash
python manage.py runserver
```

Access the app:

Open your browser and navigate to `http://127.0.0.1:8000/`
