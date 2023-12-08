import requests

BASE = "http://127.0.0.1:5000/api"
user_id = 9988
dog_id = 2
price = 1000

# Use requests.post for sending data in the request body

response = requests.post(BASE + f"/user/{user_id}/", json={
    "user_id": user_id, 
    "name": "femi", 
    "email": "test@gmail.com", 
    "password": "pass"
})
# response = requests.get(BASE + f"/user/{user_id}/")


# Check if the request was successful (status code 200)
if response.status_code == 200:
    try:
        # Try to parse the JSON content
        data = response.json()
        print(data)
    
    except requests.exceptions.JSONDecodeError:
        print("Error decoding JSON. Response content:", response.text)
else:
    # Print an error message with detailed information
    print(f"Request failed with status code {response.status_code}. Response content: {response.text}")
