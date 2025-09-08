import requests

# Replace with your actual API key
API_KEY = "795f5caca069a3ea868a02595998b82d"
city = "Delhi"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

print(data)
