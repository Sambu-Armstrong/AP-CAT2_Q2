# REST API Project
    Sambu Amstrong .
    168205 .
    BBIT 2.2C 

This project demonstrates a simple REST API using FastAPI, managing a Product resource where you can create a product name(POS), description and price and also retrieve the products(GET)

## Installation

1. Clone the Repository

2. **Create a Virtual Environment**:

    ```sh
    python -m venv .venv
    ```

3. **Activate the Virtual Environment**:

    - On PowerShell-
        ```sh
        .venv\Scripts\Activate
        ```
    - On Git Bash 
        ```sh
        source .venv/bin/activate
        ```

4. **Install Dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

## Running the API Server

1. **Start the Development Server**:

    ```sh
    uvicorn app:app --reload
    ```

2. **Access the API**:

    Open your browser and navigate to [http://127.0.0.1:8000]

3. **View Products**:

    To see the list of products, navigate to [http://127.0.0.1:8000/products]

## Testing the API

Use the provided `client.py` script to interact with the API, adding name, description and price of the product

1. **Add New Products**:
Open a new terminal and run

    ```sh
    python client.py
    ```
This will add new products and retrieve the list of all products.

## Endpoints

- **POST /products**: Create a new product.
- **GET /products**: Retrieve all products.

Each endpoint handles JSON requests and responses, including appropriate HTTP status codes and error handling.

.