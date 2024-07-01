import requests
import json

BASE_URL = "http://host1.open.uom.lk:8080"
ENDPOINT = "/api/products/"

# Updated product data
product_data = {
    "productName": "Araliya Basmathi Rice",
    "description": "White Basmathi Rice imported from Pakistan. High-quality rice with extra fragrance. Organically grown.",
    "category": "Rice",
    "brand": "Araliya",  # Updated brand
    "expiredDate": "2023.05.04",
    "manufacturedDate": "2022.02.20",
    "batchNumber": 324567,
    "unitPrice": 1020,
    "quantity": 200,
    "createdDate": "2022.02.24"
}

try:
    # Send PUT request to update the product
    headers = {'Content-Type': 'application/json'}
    response = requests.put(BASE_URL + ENDPOINT, data=json.dumps(product_data), headers=headers)
    
    # Raise an exception for bad status codes
    response.raise_for_status()
    
    # Print the JSON response
    print(response.json())

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)