# 📸 picTale

**picTale** is a Django-based web application that allows users to upload, view, edit, and delete photos and videos. It provides a clean, responsive user interface using Tailwind CSS and supports full **CRUD operations** for media content.

## 🚀 Features

- User authentication and profile management
- Upload photos and videos with captions
- View detailed media pages with descriptions
- Responsive design for mobile and desktop
- Clean dark mode interface using Tailwind CSS
- Admin panel to manage content

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, Tailwind CSS
- **Database:** SQLite (default)
- **Version Control:** Git & GitHub

## 📁 Project Structure

```

picTale/
│──accounts/           # App to manage user login, logout
│   ├──templates/      # HTML templates
├── pic/               # Main Django app
│   ├── templates/     # HTML templates
│   ├── static/        # Static files (CSS, JS)
├── media/             # Uploaded files
│   ├── myimages       # Images folder
│   ├── myvideos       # Video folder
├── manage.py          # Django management script
└── requirements.txt   # Python dependencies

````

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/vipul-pawar/picTale.git
cd picTale
````

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

* On **Windows**:

  ```bash
  venv\Scripts\activate
  ```
* On **macOS/Linux**:

  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Hosted on Render 
> https://pictale.onrender.com/ (👈 feel UI here)
site will take 30-50 second to load initially as it is hosted on free-tier 

## 🖼️ Screenshots

> ![alt text](<screenshoots/picTale.in and 2 more pages - Personal - Microsoft​ Edge 04-06-2025 4.23.49 PM.png>)

## 👤 Author

**Vipul Pawar**
🔗 [Linkedin](https://linkedin.com/in/vipul-pawar-gcoea)