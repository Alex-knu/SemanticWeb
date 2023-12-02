# creating repository

import requests

# Define the URL of the GraphDB server
url = "http://localhost:7200/rest/repositories"

# Define the headers for the request
headers = {
    "Content-Type": "multipart/form-data",
}

# Define the path to the TTL file
ttl_file_path = "first-config.ttl"

# Open the TTL file
with open(ttl_file_path, "rb") as file:
    ttl_file = file.read()

# Define the data for the request
data = {
    "config": ("config.ttl", ttl_file, "text/turtle"),
}

# Send a POST request to the GraphDB server to create the new repository
response = requests.post(url, files=data)

# Check the response
if response.status_code == 201:
    print("Repository successfully created.")
else:
    print(f"Failed to create repository. Status code: {response.status_code}. Response text: {response.text}")


