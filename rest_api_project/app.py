from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Product(BaseModel):
    name: str
    description: str
    price: float

products = []

@app.post("/products", status_code=201)
def add_product(product: Product):
    products.append(product)
    return product

@app.get("/products", response_model=List[Product])
def get_products():
    return products

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI E-Commerce API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

