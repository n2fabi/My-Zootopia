import json
import data_fetcher



def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)
def load_html(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as html_file:
    return html_file.read()

def write_html(file_path,html_code):
    with open(file_path,"w") as html_file:
        return html_file.write(html_code)

def serialize_animal(animal_obj):
    output = ''
    output += '<li class="cards__item">\n'

    if "name" in animal_obj:
        output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'

    output += '  <p class="card__text">\n'

    characteristics = animal_obj.get("characteristics", {})

    if "diet" in characteristics:
        output += f'    <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'

    locations = animal_obj.get("locations", [])
    if locations:
        output += f'    <strong>Location:</strong> {locations[0]}<br/>\n'

    if "type" in characteristics:
        output += f'    <strong>Type:</strong> {characteristics["type"]}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'
    return output


#load data from API
name = input("Enter a name on an animal: ")

response = data_fetcher.fetch_data(name)
animals_data = response.json()

#format animal data
if animals_data == []:
    output = f"<h2>The animal {name} doesn't exist.</h2>"
else:
    output = ''
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)


#load and replace html
html = load_html("animals_template.html")
html = html.replace("__REPLACE_ANIMALS_INFO__",output)

#write html
file_path = "animals.html"
write_html(file_path,html)

print(f"Website for info about the animal {name} was successfully generated to the file {file_path}.")