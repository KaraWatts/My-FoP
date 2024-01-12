class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_age(self):
        return self._age

def std_dev(people):
    ageSum = 0

    for person in people:
        ageSum += person.get_age()

    mean = ageSum/len(people)
    sqrdVar = []

    for person in people:
        sqrdVar.append((person.get_age() - mean) ** 2)
    
    sumSqrdVar = 0

    for value in sqrdVar:
        sumSqrdVar += value
    variance = sumSqrdVar/len(sqrdVar)
    
    final = variance ** 0.5
    return final


p1 = Person("Kyoungmin", 73)
p2 = Person("Mercedes", 24)
p3 = Person("Beatrice", 48)
person_list = [p1, p2, p3]
answer = std_dev(person_list)

print(answer)