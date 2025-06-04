---

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

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Run the Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## 🖼️ Screenshots

*(Optional: Add screenshots here once available)*

## 👤 Author

**Vipul Pawar**
📎 [GitHub](https://github.com/vipul-pawar)
📫 [LinkedIn](https://www.linkedin.com/in/vipul-pawar/) *(optional)*

## 📃 License

This project is licensed under the [MIT License](LICENSE).

```
