import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def fetch_data(animal_name):
    """Fetches animal data from the API Ninjas Animals API."""
    if not API_KEY:
        print("Error: API_KEY was not found in the .env file.")
        return []

    api_url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {"X-Api-Key": API_KEY}

    try:
        response = requests.get(api_url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while fetching data from API: {e}")
        return []
