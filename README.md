# 🚀 Django Master All-in-One Form

![Django](https://img.shields.io/badge/Django-4.x-green)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Database](https://img.shields.io/badge/Database-SQLite-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-success)

A complete Django-based **All-in-One Form Management System** that allows users to submit, edit, update, and manage data including file uploads within a clean and scalable architecture.

This project demonstrates practical implementation of:
- Django Forms
- CRUD Operations
- File & Image Upload Handling
- Admin Customization
- Static & Media Configuration
- Production-ready structure

---

# 📌 Features

- ✅ All-in-One Dynamic Form
- ✅ Create / Read / Update / Delete (CRUD)
- ✅ Image Upload Support
- ✅ File Upload (PDF, Documents)
- ✅ Django Form Validation
- ✅ Admin Panel Integration
- ✅ Responsive Bootstrap UI
- ✅ SQLite Database
- ✅ Static & Media File Handling
- ✅ Clean MVT Architecture

---

# 🛠️ Tech Stack

| Layer        | Technology |
|--------------|------------|
| Backend      | Django |
| Language     | Python |
| Database     | SQLite |
| Frontend     | HTML, CSS, Bootstrap |
| Version Ctrl | Git & GitHub |

---

# 📁 Project Structure

Django_Form_updated/
│
├── manage.py  
├── db.sqlite3  
├── requirements.txt  
│  
├── Django_Form_updated/  
│   ├── __init__.py  
│   ├── settings.py  
│   ├── urls.py  
│   ├── asgi.py  
│   └── wsgi.py  
│  
├── create_form/  
│   ├── migrations/  
│   ├── admin.py  
│   ├── apps.py  
│   ├── forms.py  
│   ├── models.py  
│   ├── views.py  
│   ├── urls.py  
│   └── tests.py  
│  
├── templates/  
├── static/  
└── media/  

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd Django_Form_updated
```

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt not available:

```bash
pip install django
```

## 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## 5️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

## 6️⃣ Run Development Server

```bash
python manage.py runserver
```

Open:
http://127.0.0.1:8000/

Admin:
http://127.0.0.1:8000/admin/

---

# 📂 Static & Media Configuration

### settings.py

```python
import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

### urls.py

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # app urls here
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

# 🔐 Admin Customization Example

```python
from django.contrib import admin
from .models import YourModel

@admin.register(YourModel)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    search_fields = ('name', 'email')
```

---

# 🌐 Production Deployment (Basic)

Install Gunicorn:

```bash
pip install gunicorn
```

Run:

```bash
gunicorn Django_Form_updated.wsgi
```

Recommended production stack:
- Nginx
- Gunicorn
- HTTPS (Certbot)
- VPS (Ubuntu) or PythonAnywhere

---

# 📦 Create requirements.txt

```bash
pip freeze > requirements.txt
```

Example:

```
Django>=4.0
gunicorn
```

---

# 🔮 Future Improvements

- User Authentication System
- Role-Based Access Control
- Django REST Framework API
- AJAX Form Submission
- Pagination & Search
- Email Notification
- Docker Support

---

# 🎯 Learning Outcomes

This project helps you practice:
- Django Forms
- Model-View-Template Architecture
- File Upload Handling
- Admin Customization
- Database Integration
- Production Setup

---

# 👨‍💻 Author

Md Hasibul Hasan  
Undergraduate Student  
Django Backend Developer (Learning Phase)

---

# 📜 License

This project is created for educational and portfolio purposes.
