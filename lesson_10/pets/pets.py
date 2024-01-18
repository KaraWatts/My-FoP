import json

class DuplicateNameError(Exception):
    pass

class NoSuchPet:
    pass


class NeighborhoodPets:

    def __init__(self):
        self._petData = {}

    def add_pet(self, petName, species, ownerName):
        if petName in self._petData:
            raise DuplicateNameError("Pet Name already exists")
        else: 
            self._petData[petName] = {
                "species" : species,
                "owner" : ownerName
            }
                
    def delete_pet(self, petName):
        if petName not in self._petData:
            raise NoSuchPet("Pet Name does not exist")
        else:
            del self._petData[petName]

    def get_owner(self, petName):
        if petName not in self._petData:
            raise NoSuchPet("Pet Name does not exist")
        else:
            return self._petData[petName].get('owner')


    def save_as_json(self, fileName):
        with open(f"{fileName}.json", 'w') as json_file:
            json.dump(self._petData, json_file, indent = 2)

    def read_json(self, fileName):
        with open(f'{fileName}.json', 'r') as json_file:
            self._petData = json.load(json_file)

    def get_all_species(self):
        speciesSet = []
        for petObject in self._petData.values():
            speciesSet.append(petObject["species"])
        return set(speciesSet)
    
    

np = NeighborhoodPets()

# np.add_pet('Jaxson', 'Dog', 'Kara')
# np.add_pet('Mo', "Fish", "John")
np.add_pet('Vixen', "Dog", "Tobie")

# np.save_as_json('neighborhoodpets')

np.read_json('neighborhoodpets')

print(np.get_all_species())
