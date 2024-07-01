import json

myVar = '[{"name": "Bob", "languages": ["English", "French"]}, {"name": "Alice", "languages": ["Spanish", "German"]}]'

try:
    # Parse the JSON string into a list of dictionaries
    data = json.loads(myVar)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
    exit()

# Check if the parsed data is a list
if isinstance(data, list):
    num_objects = len(data)
else:
    num_objects = 0  # Handle unexpected cases

print(num_objects)
