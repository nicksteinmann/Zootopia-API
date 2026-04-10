import data_fetcher


def serialize_animal(animal):
    """Converts one animal object into an HTML list item."""
    output = []

    output.append('<li class="cards__item">')

    if "name" in animal:
        output.append(f'    <div class="card__title">{animal["name"]}</div>')

    output.append('    <p class="card__text">')

    if "characteristics" in animal and "diet" in animal["characteristics"]:
        output.append(f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>")

    if "locations" in animal and len(animal["locations"]) > 0:
        output.append(f"<strong>Location:</strong> {animal['locations'][0]}<br/>")

    if "characteristics" in animal and "type" in animal["characteristics"]:
        output.append(f"<strong>Type:</strong> {animal['characteristics']['type']}<br/>")

    output.append('    </p>')
    output.append('</li>')

    return "\n".join(output)


def main():
    animal_name = input("Enter a name of an animal: ")
    animals_data = data_fetcher.fetch_data(animal_name)

    if len(animals_data) == 0:
        output = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'
    else:
        output_parts = []

        for animal in animals_data:
            output_parts.append(serialize_animal(animal))

        output = "\n".join(output_parts)

    # Read HTML template
    with open("animals_template.html", "r") as file:
        html_template = file.read()

    # Replace placeholder with data
    html_content = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

    # Write new HTML file
    with open("animals.html", "w") as file:
        file.write(html_content)

    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()
