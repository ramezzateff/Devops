# 📝 Flask Notes App with Docker

A simple note-taking web application built using **Flask** and **SQLite**, containerized with **Docker** for easy setup and deployment.

---

## 🚀 Features

- Add, edit, and delete notes.
- Data stored locally in `SQLite`.
- Styled with basic CSS.
- Fully containerized using `Docker` and `docker-compose`.

---

## 📁 Project Structure

├── Dockerfile
├── app
│   ├── README.md
│   ├── __pycache__
│   │   ├── db.cpython-311.pyc
│   │   └── logic.cpython-311.pyc
│   ├── db.py
│   ├── logic.py
│   ├── main.py
│   ├── notes.db
│   ├── requirements.txt
│   ├── static
│   │   └── style.css
│   └── templates
│       ├── edit.html
│       └── index.html
└── docker-compose.yml


---

## 🧰 Requirements

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ramezzateff/Devops.git
cd Devops/2-Docker/
```
### 2. Build and Run the Container
```bash
docker-compose up --build
```
### 3. Access the App
Open your browser and go to:

```bash
http://localhost:5000
```
### 🧹 Clean Up
To stop the app:

```bash
docker-compose down
```
