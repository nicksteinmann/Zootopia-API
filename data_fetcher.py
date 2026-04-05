import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')


def fetch_data(animal_name):
    """Fetches animal data from the API Ninjas Animals API."""
    api_url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(api_url, headers=headers)
    return response.json()
