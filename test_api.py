import requests

url = "http://127.0.0.1:5000/predict"

# Dummy input (42 features)
data = {str(i): 1 for i in range(42)}

response = requests.post(url, json=data)

print(response.json())