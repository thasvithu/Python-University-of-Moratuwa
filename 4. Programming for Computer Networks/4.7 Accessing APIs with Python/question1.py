import requests
import json

BASE_URL = "http://host1.open.uom.lk:8080"
ENDPOINT = "/api/products/"

# Product data in JSON format
product_data = {
    "productName": "Araliya Basmathi Rice",
    "description": "White Basmathi Rice imported from Pakistan. High-quality rice with extra fragrance. Organically grown.",
    "category": "Rice",
    "brand": "CIC",
    "expiredDate": "2023.05.04",
    "manufacturedDate": "2023.02.20",
    "batchNumber": "324567",
    "unitPrice": 1020,
    "quantity": 200,
    "createdDate": "2022.02.24"
}

try:
    # Send POST request to create new product
    headers = {'Content-Type': 'application/json'}
    response = requests.post(BASE_URL + ENDPOINT, data=json.dumps(product_data), headers=headers)
    
    # Raise an exception for bad status codes
    response.raise_for_status()
    
    # Print the response code
    print(response.status_code)

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)