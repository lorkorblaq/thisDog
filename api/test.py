import requests

BASE = "http://127.0.0.1:5000/api"
user_id = 9988
dog_id = 2
price = 1000


# response = requests.post(BASE + f"/users/", json={
#     "name":"baddest", 
#     "email":"ooko.mail", 
#     "password":"passer",
# })

# response = requests.put(BASE + f"/user/1/", json={
#     "name":"beast", 
#     "email":"olofemi.mail", 
#     "password":" road",
# })

# response = requests.get(BASE + f"/user/1/")
# response = requests.delete(BASE + f"/user/3/")



# response = requests.post(BASE + f"/dogs/", json={
#     "name":"Amica", 
#     "image":"/websites/image/dogs/alstatian.jpg",
#     "descrip": "this is a shy dog", 
#     "breed":"local", 
#     "aggression":1, 
#     "intel":2
# })

# response = requests.put(BASE + f"/dog/1/", json={
#     "name":"Amica", 
#     "breed":"tomfor", 
#     "descrip":"very shy dog",
#     "intel":89
# })

# response = requests.delete(BASE + "/dog/3/")
# response = requests.delete(BASE + "/dog/")


# response = requests.get(BASE + f"/dog/get/{dog_id}")





# response = requests.post(BASE + "/bids/", json={
#     "id_user": 2,
#     "id_dog": 1,
#     "current_price": 90000,
# })

# response = requests.get(BASE + f"/bid/50")
# response = requests.delete(BASE + f"/bid/7/")

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