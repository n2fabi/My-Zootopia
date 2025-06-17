import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')

output = ''

for animal in animals_data:
    output += '<li class="cards__item">\n'

    if "name" in animal:
        output += f"Name: {animal['name']}<br/>\n"
    if "locations" in animal and animal["locations"]:
        output += f"Location: {animal['locations'][0]}<br/>\n"
    if "characteristics" in animal:
        characteristics = animal["characteristics"]
        if "diet" in characteristics:
            output += f"Diet: {characteristics['diet']}<br/>\n"
        if "type" in characteristics:
            output += f"Type: {characteristics['type']}<br/>\n"

    output += '</li>\n'



def load_html(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as html_file:
    return html_file.read()

html = load_html("animals_template.html")

html = html.replace("__REPLACE_ANIMALS_INFO__",output)

def write_html(file_path,html_code):
    with open(file_path,"w") as html_file:
        return html_file.write(html_code)

write_html("animals.html",html)