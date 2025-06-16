# 🌸 GlowMe – Personalized Skincare & Wellness Tracker (Flask API)

GlowMe is a simple RESTful API built using **Flask** that allows users to view skincare routines based on skin types and log their wellness habits like water intake, sleep hours, and exercise.

This project is part of **Assignment 4 – SCD (Software Construction and Development)**.

---

## 🚀 Features

### 🌿 Skincare Routines
- `GET /routine/<skin_type>` – View skincare routine based on skin type (dry, oily, combination)

### 💪 Wellness Tracking
- `GET /wellness` – View all wellness logs
- `POST /wellness` – Add a new wellness log (date, water intake, hours slept, exercise done)
- `DELETE /wellness/<date>` – Delete a wellness log by date

---

## 🧪 Sample Endpoints

### 🔸 Get Routine for Dry Skin
```http
GET /routine/dry
