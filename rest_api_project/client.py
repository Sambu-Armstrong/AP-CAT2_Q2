import requests

# List of new products
products = [
    {
        "name": "Soap",
        "description": "Bathing soap for daily use.",
        "price": 80.00
    },
    {
        "name": "Shampoo",
        "description": "Hair shampoo for all hair types.",
        "price": 300.00
    },
    {
        "name": "Toothpaste",
        "description": "Mint flavored toothpaste.",
        "price": 250.00
    }
]

# Add each product to the API
for product in products:
    response = requests.post("http://127.0.0.1:8000/products", json=product)
    print(f"POST /products: {response.status_code} {response.json()}")

# Retrieve and print all products
response = requests.get("http://127.0.0.1:8000/products")
print(f"GET /products: {response.status_code} {response.json()}")

# Retrieve and print message from root endpoint
response = requests.get("http://127.0.0.1:8000")
data = response.json()
print(data["message"])



