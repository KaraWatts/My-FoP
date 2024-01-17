import json

class NobelData:

    def __init__(self, nobels_file):
        with open(nobels_file, 'r') as infile:
            self._nobels = json.load(infile)

    def search_nobel(self, year, catagory):
        year = str(year)
        category = catagory.lower()
        list_of_names = []
        for prize in self._nobels['prizes']:
            if prize['year'] == year and prize['category'] == category:
                for laureate in prize['laureates']:
                    list_of_names.append(laureate['surname'])
        return sorted(list_of_names)





nd = NobelData('nobels.json')
print(nd.search_nobel(2021, 'chemistry'))