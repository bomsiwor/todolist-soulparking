# 📝 To-Do List API 🚀
A simple and efficient To-Do List API built using **Python**, **FastAPI**, and **Pydantic**. This app helps you manage your to-dos effortlessly while showcasing modern API development principles! 🌟

---

## ⚙️ Features
- Create, Read, Update, Delete, and Finish your to-dos.
- Ultra-fast with **FastAPI**.
- Structured validation with **Pydantic**.
- Supports **ULID** for unique IDs.
- Utilize **array**, no need for database.
- Use pre-commit hooks to ensure consistency and enhance code style
- Fully Dockerized for seamless deployment. 🐳
- CI/CD to VPS using docker

**Try live API version** :
Unfortunately the VPS got suspended on 2024-12-22 💀
[🌎 LIVE DEMO API](http://193.168.195.13:8088)

---

## 📦 Packages Used
Here’s a breakdown of the amazing tools we used:

1. **Python** 🐍
   - The foundation of this app.

2. **FastAPI** ⚡
   - A modern, fast (high-performance) web framework for building APIs.
   - Automatic interactive API documentation with Swagger and ReDoc.

3. **Pydantic** ✅
   - Data validation and settings management using Python type annotations.

4. **Uvicorn** 🌐
   - An ASGI server to run FastAPI apps lightning-fast.

5. **uv** 🌟
   - A simple utility to manage ASGI servers like `uvicorn` with shortcuts for development.
   - Fast because powered by Rust

---

## 🐳 Docker Support
This repository includes **Docker support**, making it easy to containerize and run the app in any environment.
With Docker, you can build the app and run it without worrying about dependencies!

### Steps to Build and Run with Docker:
1. **Build the Docker image**:
   ```bash
   docker build -f docker/Dockerfile -t todo-app .

2. Run the container

```bash
docker run -p 8088:8088 todo-app
```

3. Access the app at http://localhost:8088

4. Alternatively, you can use docker compose. Run in port 8088
```bash
docker compose -f docker/docker-compose.yaml up -d --build
```

---

## Running Locally

Before run the project using **uv** , make sure you have install the uv by reading this [UV Installation Docs](https://docs.astral.sh/uv/getting-started/installation/)
Follow this steps to run this project locally.

1. Clone the repository. And generate env
```bash
git clone https://github.com/bomsiwor/todolist-soulparking todo-app
cd todo-app
mv .env.example .env
```

2. Setup virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies
- Use pip
```bash
pip install -r requirements.txt
```

- Use uv
```bash
uv sync
```

4. Run the project
- Use python.
Because main app contain uvicorn. We can run app using python command and still get benefits of uvicorn.
```bash
python main.py
```

- Use uv
```bash
uv start main.py
```

5. Access the API
- Swagger UI: http://localhost:8888/docs
- ReDoc: http://localhost:8888/redoc
