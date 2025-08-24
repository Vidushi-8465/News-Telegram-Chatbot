import requests
import os
from dotenv import load_dotenv

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

url = f"https://newsapi.org/v2/top-headlines?country=in&pageSize=4&apiKey={NEWS_API_KEY}"
response = requests.get(url)
print("Status code:", response.status_code)
print("Response:", response.text)
