# Backend Intern CRUD
This project is a **FastAPI backend** that implements a blog management system with CRUD operations, authentication, likes, and comments.

## Features
- User Signup & Login (JWT Authentication)
- Create, Read, Update, Delete blog posts
- Like functionality (one like per user per post)
- Comment functionality
- Protected routes for write operations

## Tech Stack
- Python 3.10+
- FastAPI
- SQLAlchemy
- SQLite (default, easy to run locally)
- JWT Authentication

## Setup Instructions
-Create Virtual Environment
  python -m venv venv 
  venv\Scripts\activate
-Install Dependencies
 pip install -r requirements.txt
-Setup Environment
 SECRET_KEY=my secret key
 ALGORITHM=HS256
 ACCESS_TOKEN_EXPIRE_MINUTES=30
 DATABASE_URL=sqlite:///./blog.db
-Run the Server
 uvicorn src.main:app --reload




