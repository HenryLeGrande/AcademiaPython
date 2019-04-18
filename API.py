import MySQLdb
import requests
import json

class Api:

    def __init__(self, name):
        self.name = name
        self.url = 'https://restcountries.eu/rest/v2/name/' + self.name

    def getApi(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            self.content = response.content
            self.response_json = json.loads(self.content)
            self.dict = self.response_json[0]
            self.nombre = self.dict["name"]
            self.capital = self.dict["capital"]
            self.poblacion = self.dict["population"]

            print("Los datos del pais son: ", self.dict)

    def get_dict(self):
        return requests.get(self.url).json()[0]


