# Chris Alex - Cyberpunk Portfolio

A full-stack single-page portfolio website with a cyberpunk/techy theme.

## Project Structure

```
portfinal/
├── public/
│   ├── index.html    # Frontend HTML
│   └── style.css     # Cyberpunk CSS styles
├── backend/
│   ├── server.py     # Flask server
│   ├── database.py   # SQLite database functions
│   └── portfolio.db  # Database (created automatically)
├── requirements.txt  # Python dependencies
└── README.md
```

## Setup & Run

### 1. Install Python Dependencies

Open terminal in VS Code (Ctrl + `) and run:

```bash
cd C:\Users\chris\OneDrive\Desktop\portfinal
pip install -r requirements.txt
```

### 2. Start the Server

```bash
python backend/server.py
```

### 3. View the Website

- **Portfolio:** http://localhost:5000
- **Admin Panel:** http://localhost:5000/admin (view contact messages)

## Features

- **Cyberpunk Theme:** Neon colors, glitch effects, animated grid background
- **Contact Form:** Stores messages in SQLite database
- **Visitor Counter:** Tracks page visits
- **Responsive Design:** Works on mobile and desktop
- **Admin Panel:** View all contact submissions

## Tech Stack

- **Frontend:** HTML5, CSS3, JavaScript
- **Backend:** Python, Flask
- **Database:** SQLite
