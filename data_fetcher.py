import requests

API_KEY = "a30Bxc2MCQw3ON4KGYXSXRGeN8W7JIlcDkElvBKU"


def fetch_data(animal_name):
    """Fetches animal data from the API Ninjas Animals API."""
    api_url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(api_url, headers=headers)
    return response.json()
