```markdown
# 📸 picTale

**picTale** is a Django-based web application designed to let users upload, share, and view photos and videos. It’s optimized for responsive design and styled using Tailwind CSS for a modern and minimal UI experience.

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
├── pic/               # Main Django app
│   ├── templates/     # HTML templates
│   ├── static/        # Static files (CSS, JS)
├── media/             # Uploaded files
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

## 🖼️ Screenshots

> *(Coming soon – add your app screenshots here to showcase the UI and features)*

## 👤 Author

**Vipul Pawar**
🔗 [GitHub](https://github.com/vipul-pawar)

## 📃 License

This project is licensed under the [MIT License](LICENSE).

```
