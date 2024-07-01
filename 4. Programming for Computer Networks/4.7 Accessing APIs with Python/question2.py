import requests

BASE_URL = "http://host1.open.uom.lk:8080"
ENDPOINT = "/api/products/"

try:
    # Send GET request to retrieve all products
    response = requests.get(BASE_URL + ENDPOINT)
    
    # Raise an exception for bad status codes
    response.raise_for_status()
    
    # Parse the JSON response
    data = response.json()
    
    # Get the list of products from the 'data' key
    products = data.get('data', [])
    
    # Print the total number of products
    print(len(products))

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)