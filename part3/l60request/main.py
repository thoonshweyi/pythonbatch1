import requests

# => GET request
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

print(f"Status Code: {response.status_code}")
datas = response.json()
# print(f"All Posts: ${datas}")
print(f"Total Posts: {len(datas)}")
print(f"First Posts: {datas[0]}")


# => GET request with parameter
postid = 3
response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{postid}")
print(f"Post ID 3: {response.json()}")

# => POST request
newpost = {
  "userId": 1,
  "title": "My Text Post",
  "body": "This is just a text"
}
response = requests.post('https://jsonplaceholder.typicode.com/posts',json=newpost) # automatically converts the dictionary to json
print(f"Create Post : {response.json()}")
print(f"Total Posts : {len(datas)}")
# Create Post : {'userId': 1, 'title': 'My Text Post', 'body': 'This is just a text', 'id': 101}
# Total Posts : 100

# id 101 and server's post didn't affect.

# => PUT request

updatepost = {
"id":5,
  "userId": 1,
  "title": "Update Test Post",
  "body": "This is just a test"
}
response = requests.put('https://jsonplaceholder.typicode.com/posts/5',json=updatepost) # automatically converts the dictionary to json
print(f"Update Post : {response.json()}")    #Update Post : {'id': 5, 'userId': 1, 'title': 'Update Test Post', 'body': 'This is just a test'}


# DELETE request

response = requests.delete('https://jsonplaceholder.typicode.com/posts/10') 
print(f"Delete Status Code : {response.status_code}")   #Delete Status Code : 200

