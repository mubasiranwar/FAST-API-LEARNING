
# 🚀 FastAPI & Machine Learning Mastery

### ⚡ Building APIs • 🧠 Deploying ML Models • 🐳 Dockerized Applications

Welcome to my **FastAPI & Machine Learning learning repository**.
This repository serves as a **comprehensive portfolio** showcasing my journey in building **robust REST APIs**, **serving Machine Learning models**, and **deploying production-ready applications using Docker**.

The focus of this repository is **practical implementation**, clean architecture, and real-world backend + ML workflows.

---

## 📌 Projects Overview

This repository contains **two complete, real-world projects**, each targeting a different aspect of backend and ML development:

1. 💻 **Laptop Price Predictor** – End-to-End ML Application
2. 🏥 **Patient Management System** – FastAPI CRUD-Based Backend API

---

## 💻 Project 1: Laptop Price Prediction

### 🔹 End-to-End Machine Learning Application

This project demonstrates a **full-stack Machine Learning workflow**, from model inference using **FastAPI** to a **user-friendly Streamlit frontend**, all packaged using **Docker**.

### ✨ Key Features

* 🧠 **Machine Learning Integration**
  Serves a trained regression model to predict laptop prices based on input specifications.

* ⚡ **FastAPI Backend**
  Handles high-performance API requests for real-time model inference.

* 🎨 **Streamlit Frontend**
  Clean, interactive UI allowing users to input features and instantly view predictions.

* 🐳 **Dockerized Deployment**
  Fully containerized for seamless, plug-and-play execution.

* 📦 **Docker Hub Hosting**
  Pre-built image available for quick testing and deployment.

---

### 🐳 Docker Hub Repository

The official Docker image for the ML prediction project is available here:

👉 **mubasir123/iris on Docker Hub**
[https://hub.docker.com/repository/docker/mubasir123/iris/general](https://hub.docker.com/repository/docker/mubasir123/iris/general)

#### ▶️ Pull the Image

```bash
docker pull mubasir123/iris:latest
```

#### ▶️ Run the Container

```bash
docker run -p 8501:8501 mubasir123/iris:latest
```

---

## 🏥 Project 2: Patient Management System

### 🔹 FastAPI CRUD-Based Healthcare API

This project focuses on **advanced FastAPI concepts**, strong **data validation**, and **automated health metric computation**, simulating a real healthcare backend service.

---

### ✨ Key Features

* 🔄 **Full CRUD Operations**
  Create, Read, Update, and Delete patient records stored in a local JSON database.

* 🛡️ **Pydantic-Powered Validation**
  Enforces strict constraints on:

  * Age
  * Gender
  * Height
  * Weight

* 🧮 **Computed Health Metrics**

  * Automatic **BMI calculation**
  * Real-time **Health Verdict**:

    * Underweight
    * Normal
    * Overweight
    * Obesity

* 🔍 **Advanced Querying**
  Includes a `/sort` endpoint to dynamically sort patients by:

  * Age
  * Height
  * Weight

* ⚠️ **Proper Error Handling**
  Uses correct HTTP status codes and meaningful exception messages.

---

## 📂 Repository Structure

```
.
├── END TO END ML PROJECT/         # Project 1: ML Prediction System
│   ├── api/                       # FastAPI backend
│   ├── model/                     # Trained model (.pkl) & prediction logic
│   ├── schema/                    # Pydantic input/output schemas
│   └── streamlit_app/             # Streamlit UI & Docker setup
│
└── PATIENT MANGMENT PROJECT/      # Project 2: Patient Management API
    ├── Project_patients.py        # Main FastAPI application
    ├── patients.json              # Local data storage
    └── practice.py                # Experimental scripts
```

---

## 🛠️ How to Run

### ▶️ Running the Patient Management API (Locally)

```bash
cd "PATIENT MANGMENT PROJECT"
pip install -r requirements.txt
uvicorn Project_patients:app --reload
```

📄 Access the interactive Swagger documentation at:

```
http://127.0.0.1:8000/docs
```

---

### ▶️ Running the ML Project (Dockerized)

```bash
docker run -p 8501:8501 mubasir123/iris:latest
```

Then open your browser at:

```
http://localhost:8501
```

---

## 🎯 Key Learnings from This Repository

✔ FastAPI fundamentals & advanced features
✔ REST API design best practices
✔ Pydantic schema validation & computed fields
✔ Serving ML models with FastAPI
✔ Streamlit–FastAPI integration
✔ Dockerizing ML & backend applications
✔ Production-style project structuring

---

## 🚀 Future Enhancements

* Database integration (PostgreSQL / MongoDB)
* Authentication & Authorization
* Asynchronous ML inference
* API versioning
* CI/CD pipelines
* Cloud deployment (AWS / Render / GCP)

---

## 👨‍💻 Author

**Mubasir Anwar**
FastAPI Enthusiast | Machine Learning Engineer

🔗 **Docker Hub Profile:**
[https://hub.docker.com/u/mubasir123](https://hub.docker.com/u/mubasir123)


Just say the word 🚀
