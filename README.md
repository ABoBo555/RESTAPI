# Enterprise Employee Management REST API

A production-inspired RESTful API built with **FastAPI**, **Microsoft SQL Server**, and **JWT Authentication** following a clean layered architecture.

This project demonstrates how enterprise backend applications are structured by separating responsibilities into routers, services, mappers, database operations, SQL queries, and stored procedures. It implements secure authentication, role-based authorization (RBAC), employee management, and user administration while following clean coding practices and maintainable project architecture.

---

## Featuresq

### Employee Management

- Create Employee
- Retrieve Employee by ID
- Retrieve Employee List
- Update Employee
- Soft Delete Employee
- Pagination
- Searching
- Filtering
- Sorting
- Request Validation
- Centralized Exception Handling

---

### User Management

- Create User (Admin)
- Public User Registration
- Retrieve User by ID
- Retrieve User List
- Update User
- Soft Delete User
- Get Current Logged-in User (`/users/me`)
- Change Password
- Password Strength Validation

---

### Authentication

- User Registration
- User Login
- BCrypt Password Hashing
- JWT Access Token
- JWT Refresh Token Generation
- Current User Dependency
- Protected Endpoints

---

### Authorization (RBAC)

Implemented Role-Based Access Control with the following roles:

- Admin
- HR
- Manager
- Employee
- Auditor

Protected endpoints use dependency-based authorization to restrict access according to business rules.

Example:

- Employee → View employee information
- HR → Manage users
- Admin → Full system access

---

### Security

- BCrypt Password Hashing
- JWT Authentication
- Password Verification
- Password Strength Validation
- OAuth2 Bearer Authentication
- Protected Routes
- Current User Extraction
- Secure Password Change
- Soft Delete Protection

Password Policy:

- Minimum 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one number
- At least one special character
- Rejects commonly used passwords

---

## Technology Stack

### Backend

- FastAPI
- Python 3.12

### Database

- Microsoft SQL Server
- Stored Procedures
- Parameterized Queries

### Authentication

- JWT (JSON Web Token)
- OAuth2 Password Bearer
- Passlib (BCrypt)

### Validation

- Pydantic v2

### Database Driver

- pyodbc

---

# Project Architecture

The project follows a layered architecture commonly used in enterprise applications.

```
Client
    │
    ▼
Routers
    │
    ▼
Services
    │
    ▼
Mappers
    │
    ▼
Database Operations
    │
    ▼
SQL Queries
    │
    ▼
Stored Procedures
    │
    ▼
SQL Server
```

Each layer has a single responsibility.

| Layer | Responsibility |
|--------|----------------|
| Routers | API Endpoints |
| Services | Business Logic |
| Mappers | Convert Database Rows into Pydantic Models |
| Database Operations | Execute SQL Queries |
| Queries | SQL Statements |
| Stored Procedures | Database Business Logic |

---

# Project Structure

```
RESTAPI/
│
├── app/
│   ├── database/
│   │   ├── operations/
│   │   └── queries/
│   │
│   ├── exceptions/
│   │
│   ├── mappers/
│   │
│   ├── routers/
│   │
│   ├── schemas/
│   │
│   ├── security/
│   │
│   ├── services/
│   │
│   ├── config.py
│   ├── logging_config.py
│   └── main.py
│
├── database_scripts/
│   ├── Employee/
│   └── Users/
│
├── requirements.txt
└── README.md
```

---

# Database Design

## Employee

Supports:

- Create
- Read
- Update
- Soft Delete
- Pagination
- Search
- Filtering

---

## Users

Supports:

- Registration
- Login
- Role Management
- Password Change
- Soft Delete
- Last Login Tracking

---

# API Endpoints

## Health

| Method | Endpoint |
|---------|----------|
| GET | `/health` |

---

## Authentication

| Method | Endpoint |
|---------|----------|
| POST | `/auth/register` |
| POST | `/auth/login` |

---

## Employees

| Method | Endpoint |
|---------|----------|
| GET | `/employees` |
| GET | `/employees/{id}` |
| POST | `/employees` |
| PUT | `/employees/{id}` |
| DELETE | `/employees/{id}` |

---

## Users

| Method | Endpoint |
|---------|----------|
| GET | `/users` |
| GET | `/users/me` |
| GET | `/users/{id}` |
| POST | `/users` |
| PUT | `/users/{id}` |
| DELETE | `/users/{id}` |
| PUT | `/users/me/password` |

---

# Authentication Flow

```
Register
     │
     ▼
User Created
     │
     ▼
Login
     │
     ▼
JWT Access Token
JWT Refresh Token
     │
     ▼
Authorize Swagger
     │
     ▼
Access Protected APIs
```

---

# Authorization Flow

```
JWT Token
      │
      ▼
get_current_user()
      │
      ▼
Extract Role
      │
      ▼
require_roles(...)
      │
      ▼
Allow / Deny Access
```

---

# Password Security

Passwords are never stored in plain text.

Workflow:

```
Password

↓

BCrypt Hash

↓

Database
```

Password verification uses BCrypt secure comparison.

---

# Soft Delete Strategy

Instead of permanently deleting records, the project implements soft deletion.

```
IsActive = 0
IsDeleted = 1
```

Deleted users and employees remain available for auditing while being excluded from normal application operations.

---

# Validation

Implemented using **Pydantic v2**.

Examples:

- Email validation
- Password validation
- Pagination validation
- Positive ID validation
- Enum validation
- Required fields

---

# Exception Handling

Centralized exception handling for:

- Authentication Errors
- Authorization Errors
- Validation Errors
- User Not Found
- Employee Not Found
- Duplicate User
- Invalid Password
- Invalid Token

---

# Security Features

- JWT Authentication
- BCrypt Password Hashing
- OAuth2 Bearer Authentication
- Role-Based Authorization (RBAC)
- Password Strength Validation
- Soft Delete Protection
- Secure Password Update

---

# Current Implemented Modules

- Employee Module
- User Module
- Authentication Module
- Authorization (RBAC)
- Health Check Module
- Security Module
- Password Reset

---

# Future Improvements

Planned enhancements include:

- Refresh Token Rotation
- Logout Endpoint
- Email Verification
- Audit Logging
- Request Logging
- Docker Support
- Unit Testing
- Integration Testing
- CI/CD Pipeline
- Deployment
- API Versioning
- Redis Caching

---

# Learning Objectives

This project demonstrates practical experience with:

- FastAPI
- REST API Design
- Layered Architecture
- SQL Server
- Stored Procedures
- JWT Authentication
- RBAC
- Dependency Injection
- Pydantic Validation
- Exception Handling
- Clean Code Principles
- Enterprise Backend Development

---

# How to Run

## Clone

```bash
git clone https://github.com/ABoBo555/RESTAPI.git
```

```bash
cd RESTAPI
```

## Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create a `.env` file.

Example:

```env
DB_SERVER=YOUR_SERVER
DB_DATABASE=HR_DB
DB_TRUSTED_CONNECTION=yes

JWT_SECRET_KEY=your_secret_key
JWT_ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
```

---

## Create Database

Run the SQL scripts located in:

```
database_scripts/
```

in the following order:

1. Database
2. Tables
3. Stored Procedures
4. Seed Data

---

## Run Application

```bash
uvicorn app.main:app --reload
```

---

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# License

This project is intended for educational and portfolio purposes.

---

# Author

**Aung Bo Bo**

Backend Developer | Python | FastAPI | SQL Server | REST API Development