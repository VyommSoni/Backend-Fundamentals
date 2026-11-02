# FastAPI Serialization & Deserialization Engine

A clean, production-ready demonstration of **Serialization** and **Deserialization** in a Python REST API using **FastAPI** and **Pydantic**. 

---

## 🚀 Overview

In modern web development, data is constantly moving across boundaries:
1. **Clients** send raw JSON payloads over HTTP.
2. **Servers** must parse, validate, and convert that text into language-native objects (**Deserialization**).
3. **Servers** process the data, perform business logic or database queries, and convert Python objects back into structured JSON strings for HTTP responses (**Serialization**).

In this project, **Pydantic** acts as our core validation and translation engine, seamlessly integrated with **FastAPI**.

---

## 🛠️ Tech Stack

* **Python 3.x**
* **FastAPI**: Modern, high-performance web framework for building APIs.
* **Pydantic**: Data validation and parsing using Python type annotations.
* **Uvicorn**: Lightning-fast ASGI server implementation.

---

## 📂 Code Implementation (`main.py`)

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
from uvicorn import run as app_run

app = FastAPI(
    title="Serialization and Deserialization"
)

class UserCreate(BaseModel):
    # Deserialization Schema: Validates incoming raw client JSON
    name: str = Field(..., example="John Doe")
    Age: int = Field(..., gt=0, description="Age must be greater than 0")
    email: EmailStr = Field(..., example="john.doe@example.com")

class UserResponse(BaseModel):
    # Serialization Schema: Formats and controls outgoing response JSON
    id_: int = Field(..., gt=0, description="Id must be greater than 0")
    name: str = Field(..., example="John Doe")
    email: EmailStr = Field(..., example="john.doe@example.com")
    is_active: bool = Field(..., description="Indicates if the user is active")

# In-memory mock database
DB = []
id_counter = 1  # Fixed starting point for IDs

@app.post("/users", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate):
    global id_counter
    
    new_user = {
        "id_": id_counter,
        "name": user.name,
        "email": user.email,
        "is_active": True
    }

    DB.append(new_user)
    id_counter += 1

    return new_user

if __name__ == "__main__":
    app_run("main:app", host="127.0.0.1", port=8001, reload=True)
```

---

## 🔍 How Serialization & Deserialization Work Here

### 1. Deserialization (Client ➔ Server)
When a client sends a `POST` request to `/users` with a JSON payload:
* **FastAPI** intercepts the raw HTTP body.
* **Pydantic** (`UserCreate`) deserializes the JSON string and validates every property against the defined constraints (e.g., ensuring `Age` is greater than 0 and `email` is structurally valid).
* If any rule fails, FastAPI automatically halts execution and returns a structured `422 Unprocessable Entity` error.

### 2. Serialization (Server ➔ Client)
When the endpoint successfully processes the request:
* The function creates a dictionary (`new_user`) containing the database record.
* FastAPI reads the `response_model=UserResponse` parameter.
* **Pydantic** serializes the response data, ensuring only the fields specified in `UserResponse` are returned in the final JSON body sent back to the client.

---

## 🚀 How to Run the Project

1. **Install Dependencies:**
   ```bash
   pip install fastapi uvicorn pydantic email-validator
   ```

2. **Run the Server:**
   Save your code in a file named `main.py` and execute:
   ```bash
   python main.py
   ```

3. **Explore Interactive Docs:**
   Open your browser and navigate to:
   * Swagger UI: [http://127.0.0.1:8001/docs](http://127.0.0.1:8001/docs)
   * ReDoc: [http://127.0.0.1:8001/redoc](http://127.0.0.1:8001/redoc)