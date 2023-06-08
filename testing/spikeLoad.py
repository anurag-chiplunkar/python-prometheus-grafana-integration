import requests

payload = {
    'percentage': 70,
    'duration': 5
}

response = requests.post('http://localhost:5000/increase-cpu', json=payload)
print(response.text)
