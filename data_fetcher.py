import requests

api_key = "Y5Tzh0xkyRsNErgMavh+7w==Mm73JEFprF65dUyY"

def fetch_data(animal_name):
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal_name)
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)
    return response