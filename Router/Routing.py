from fastapi import FastAPI,Query,Path
from uvicorn import run as app_run


#Routing : Where you want to Go on the server, this is the understanding of the routing in Rest APIs
# Initialize FastAPI app with metadata 

app = FastAPI(
    title="Mastering APIs - Routing Guide",
    description="A complete reference implementation for static, dynamic, query, nested, versioned, and catch-all routes.",
    version="1.0.0"
)



# This is static Route where it doesnt change it gives you same data constantly 
@app.get("/home",tags=["Static Route"])
def home():
    return "Hi Vyommm,Welcome to our page"   


#Dyanamic Route : This is the route which changes based on the input given by the user
                  # we given Path in URL itself to do so which is called path paramter 

#Tips for myself : Always Validate the input given by the user to avoid any errors in the code and also to avoid any security issues
                   # Using PATH library we can validate the input given by the user in the URL itself
@app.get("/profile/v1/{name}",tags=["Dynamic Route"])
def user_name(name:str=Path(...,title="Name of the User",description="This is the name of the user which is dynamic in nature")):
    return f"Hi {name},Welcome to the Profile"



#Query Parameter : This is the parameter which is given by the user in the URL after the ? symbol and it can be optional or mandatory
                   # used for Filtering, searching, sorting, and pagination in API'S

@app.get("/search/v1/products",tags=["Query Parameter"])
def search_products(category:str=Query(...,title="Name of the Product",description="This is the name of the product which is dynamic in nature"),price:int=Query(...,gt=0,title="Price of the Product",description="This is the price of the product which is dynamic in nature")):
    return f"Hi Vyommm,You are searching for {category} with price {price}"



#Nested Routes : This is the route which is nested inside another route and it is used to get the data of a specific resource which is nested inside another resource

@app.get("/api/v1/products/{product_id}/reviews/{review_id}", tags=["Nested Routes"])
def get_product_review(
    product_id: int = Path(..., gt=0),
    review_id: int = Path(..., gt=0)
):
    return {
        "product_id": product_id,
        "review_id": review_id,
        "author": "Vyom",
        "rating": 5,
        "comment": "Absolute masterpiece of an API architecture!"
    }

# ROUTE VERSIONING
# ==========================================
# Definition: Prefixing routes with a version identifier (`/v1/`, `/v2/`) to prevent breaking old clients when updates happen.
# Industry Use Case: Upgrading your data schema or response structure safely without crashing mobile apps or frontend clients already in production.

@app.get("/api/v1/posts", tags=["Versioning"])
def get_posts_v1():
    # Legacy response structure
    return [{"id": 1, "title": "Hello World v1"}]

@app.get("/api/v2/posts", tags=["Versioning"])
def get_posts_v2():
    # New, improved response structure with metadata
    return {
        "version": "v2",
        "total_count": 1,
        "data": [{"post_id": 1, "headline": "Hello World v2", "author_id": 42}]
    }


if __name__=="__main__":
    app_run(app, host="127.0.0.1", port=8001)


