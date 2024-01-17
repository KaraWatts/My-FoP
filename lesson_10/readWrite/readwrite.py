
rhyme = ["Mary had a little lamb", "It's fleece was white as snow", "And everywhere that Mary went", "the lamb was sure to go."]

with open ('Mary.txt', 'w') as outfile:
    for line in rhyme:
        outfile.write(line + '\n')


with open('Mary.txt', 'r') as infile:
    for line in infile:
        print(line.strip())


names = ['William', 'Patrick', 'Jon', 'Tom', 'Peter', 'Colin', 'Sylvester', 'Paul', 'Chris', 'David', 'Matt', 'Peter', 'Jodie']

names_dictionary = {}

for index, name in enumerate(names):
    names_dictionary[index+1] = name

import json

with open('names.json', 'w') as outfile:
    json.dump(names_dictionary, outfile)

with open('names.json', 'r') as infile:
    print(json.load(infile))

