# 🚀 Backend Fundamentals: API Routing Masterclass

Welcome to the routing module of my **Backend Fundamentals** repository! This project serves as a hands-on reference implementation for mastering core API routing architectures using **FastAPI (Python)**. 

As an aspiring AI & Agentic Engineer, building clean, scalable, and production-ready routing systems is the foundation for creating robust APIs that interface smoothly with modern web clients and autonomous agents.

---

## 🗺️ Routing Concepts Covered

This repository demonstrates the following 6 essential routing patterns used in industry-grade backend development:

### 1. Static Routes
* **What it is:** Hardcoded paths that match an exact string and always return a consistent response.
* **Use Case:** Health checks, system status checks, and static landing pages.
* **Example:** `GET /health` or `GET /home`

### 2. Dynamic Routes (Path Parameters)
* **What it is:** Routes that embed variable parameters directly inside the URL path using curly braces (`{}`).
* **Best Practice:** Using FastAPI's `Path` validator to enforce type safety and constraints (e.g., ensuring IDs are positive integers greater than zero).
* **Example:** `GET /api/v1/users/{user_id}`

### 3. Query Parameters
* **What it is:** Optional or required key-value pairs appended after the `?` in a URL.
* **Best Practice:** Enforcing strict bounds checking (e.g., pagination limits) and regex validation to prevent bad inputs or server overload.
* **Example:** `GET /api/v1/products?category=electronics&limit=10`

### 4. Nested Routes
* **What it is:** Routes that reflect a hierarchical relationship (parent/child resources) within the URL structure.
* **Use Case:** Accessing child data directly tied to a specific parent resource.
* **Example:** `GET /products/{product_id}/reviews/{review_id}`

### 5. API Versioning
* **What it is:** Prefixing URL paths with version identifiers (`/api/v1/` vs `/api/v2/`) to safely roll out breaking schema changes.
* **Use Case:** Ensuring legacy mobile apps or frontend clients don't break when your backend data structures evolve.
* **Example:** `GET /api/v1/posts` vs `GET /api/v2/posts`

### 6. Catch-All Routes
* **What it is:** Wildcard matchers using path converters (`{file_path:path}`) to scoop up multi-level path segments and forward slashes.
* **Use Case:** Building file management systems, cloud storage navigation, or Single Page Application (SPA) frontend routers.
* **Example:** `GET /files/{file_path:path}`

---

## 💻 Code Implementation Preview

Here is a quick look at how these routes are structured in the FastAPI implementation (`Routing.py`):

```python

# 1. Static Route
@app.get("/home",tags=["Static Route"])
def home():
    return "Hi Vyommm,Welcome to our page"   


# 2. Dynamic Route
@app.get("/profile/v1/{name}",tags=["Dynamic Route"])
def user_name(name:str=Path(...,title="Name of the User",description="This is the name of the user which is dynamic in nature")):
    return f"Hi {name},Welcome to the Profile"


# 3. Query Parameters
@app.get("/api/v1/products")
def list_products(
    category: str = Query(..., description="Product category"),
    limit: int = Query(10, ge=1, le=100, description="Pagination limit")
):
    return {"category": category, "limit": limit}

# 4. Nested Routes
@app.get("/api/v1/products/{product_id}/reviews/{review_id}")
def get_review(product_id: int = Path(..., gt=0), review_id: int = Path(..., gt=0)):
    return {"product_id": product_id, "review_id": review_id, "rating": 5}

# 5. API Versioning (v1 vs v2)
@app.get("/api/v1/posts")
def get_posts_v1():
    return [{"id": 1, "title": "Post v1"}]

@app.get("/api/v2/posts")
def get_posts_v2():
    return {"version": "v2", "data": [{"post_id": 1, "headline": "Post v2"}]}
