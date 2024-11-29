REST API Project
Sambu Amstrong .
168205 .
BBIT 2.2C 
This project demonstrates a simple REST API using FastAPI, managing a Product resource where you can create a product name(POS), description and price and also retrieve the products(GET)

Installation
Clone the Repository:

git clone <repository_url>
cd rest_api_project
Create a Virtual Environment:

python -m venv .venv
Activate the Virtual Environment:

On PowerShell-
.venv\Scripts\Activate
On Git Bash
source .venv/bin/activate
Install Dependencies:

pip install -r requirements.txt
Running the API Server
Start the Development Server:

uvicorn app:app --reload
Access the API:

Open your browser and navigate to [http://127.0.0.1:8000]

View Products:

To see the list of products, navigate to [http://127.0.0.1:8000/products]

Testing the API
Use the provided client.py script to interact with the API, adding name, description and price of the product

Add New Products:

python client.py
This will add new products and retrieve the list of all products.

Endpoints
POST /products: Create a new product.
GET /products: Retrieve all products.
Each endpoint handles JSON requests and responses, including appropriate HTTP status codes and error handling.

.
