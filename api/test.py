import requests

BASE = "http://127.0.0.1:5000/api"
user_id = 9988
dog_id = 2
price = 1000

# Use requests.post for sending data in the request body

# response = requests.post(BASE + f"/user/create/", json={
#     "name":"blaq", 
#     "email":"fa.mail", 
#     "password":"passer",
# })

response = requests.get(BASE + f"/user/get/")




# response = requests.post(BASE + f"/dog/create/", json={
#     "name":"browner", 
#     "image":"/image/husky.jpg", 
#     "breed":"husky", 
#     "aggression":5, 
#     "intel":4
# })


# response = requests.get(BASE + f"/dog/get/{dog_id}")


# response = requests.post(BASE + "/bid/create/", json={
#     "id_user": 1,
#     "id_dog": 1,
#     "initial_price": 20,
#     "last_price": 40,
#     "current_price": 30,
#     "sold": False
# })

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