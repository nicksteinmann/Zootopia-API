import requests

API_KEY = "a30Bxc2MCQw3ON4KGYXSXRGeN8W7JIlcDkElvBKU"


def fetch_data(animal_name):
    """Fetches animal data from the API Ninjas Animals API."""
    api_url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(api_url, headers=headers)
    return response.json()


# Load animal data
animal_name = input("Enter a name of an animal: ")
animals_data = fetch_data(animal_name)


def serialize_animal(animal):
    """Converts one animal object into an HTML list item."""
    output = ""

    output += '<li class="cards__item">\n'

    if "name" in animal:
        output += f'    <div class="card__title">{animal["name"]}</div>\n'

    output += '    <p class="card__text">\n'

    if "characteristics" in animal and "diet" in animal["characteristics"]:
        output += f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n"

    if "locations" in animal and len(animal["locations"]) > 0:
        output += f"<strong>Location:</strong> {animal['locations'][0]}<br/>\n"

    if "characteristics" in animal and "type" in animal["characteristics"]:
        output += f"<strong>Type:</strong> {animal['characteristics']['type']}<br/>\n"

    output += '</p>\n'
    output += '</li>\n'

    return output


# Build output string instead of printing
output = ""

for animal in animals_data:
    output += serialize_animal(animal)

# Read HTML template
with open("animals_template.html", "r") as file:
    html_template = file.read()

# Replace placeholder with data
html_content = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

# Write new HTML file
with open("animals.html", "w") as file:
    file.write(html_content)
    print("Website was successfully generated to the file animals.html.")
