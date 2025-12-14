# Sweet Shop Management System

This project is a Sweet Shop Management System built as part of the Incubyte assignment.

The system consists of:
- A FastAPI backend with authentication, inventory management, and role-based access
- A React Single Page Application (SPA) frontend
- Automated tests using pytest
- A 3D visualization using a Sketchfab model integrated into the frontend

---

## Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication
- Pytest

### Frontend
- React (Vite)
- Fetch API
- Sketchfab (3D embed)

---

## Features

### Backend
- User registration and login
- JWT-protected routes
- Role-based access control (Admin/User)
- Create, update, delete sweets
- Search sweets by name, category, and price
- Purchase sweets with inventory tracking
- Restock sweets (Admin only)
- Automated tests for critical flows

### Frontend (SPA)
- User login
- View sweets inventory
- Purchase sweets
- Embedded 3D Sweet Shop model using Sketchfab

---

## How to Run

### Backend
```bash
cd sweet-shop-backend
python -m uvicorn app.main:app --reload

