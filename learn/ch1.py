from fastapi import FastAPI

print("Application starting...")
print("FastAPI obj creating...")

app = FastAPI()

print("FastAPI obj created...")


@app.get("/")
def home():
    print("home fun is executing...")
    return {"message": "Hello"}

@app.get("/about")
def about():
    print("about fun is executing...")
    return{"Company":"CMHL Holding",
           "rating" : 4.8
           }

#path parameter
@app.get("/employees/{emp_id}")
def get_employees(emp_id: int):
    print("get_employee fun is executing...")
    return {"emp_id_p": emp_id}

#testing path one as query style
@app.get("/employees_test")
def get_employees_test(emp_id: int = 1):
    print("get_employee fun is executing...")
    return {"emp_id_p": emp_id}

#query parameter
@app.get("/products")
def get_products(page : int, category : str = "all"):
    print("get_products fun is executing...")
    return {"category": category,
            "page": page}


#path+query parameter
@app.get("/items/{item_id}")
def get_items(item_id : int, page : int = 1, premium : bool = False):
    print("get_items fun is executing...")
    return {"item_id": item_id,
            "page": page,
            "premium": premium}


print("Application loaded")
