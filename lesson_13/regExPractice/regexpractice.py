# 1. Write a function that uses a regex expression to return the boolean True if the string that is passed in contains only upper and lowercase letters, numbers, and underscores.
# Exmaples:
# Input: 'The quick brown fox jumps over the lazy dog.'
# Output: False
# Input: 'Python_Exercise_1'
# Output: True
import re
def checkStr(str):
    regEx = r'^[\w\d\_]+$'
    match = re.match(regEx, str)

    return bool(match)

# print(checkStr('The quick brown fox jumps over the lazy dog.'))
# print(checkStr('Python_Exercise_1'))

# 2. Write a function that uses a regex expression to return the boolean True if the string that is passed in starts with the number 5.
# Exmaple:
# Input: '6-563345'
# Output: False
# Input: '5-762145'
# Output: True

def start5(str):
    regEx = r'^5'
    match = re.match(regEx, str)

    return bool(match)

# print(start5('6-563345'))
# print(start5('5-762145'))



# 3. Write a function that uses a regex expression to return the boolean True if the string that is passed in has a number at the end.
# Exmaple:
# Input: 'abcdef'
# Output: False
# Input: 'abcdef7'
# Output: True

def endNum(str):
    regEx = r'.*\d$'
    match = re.match(regEx, str)

    return bool(match)

# print(endNum('abcdef'))
# print(endNum('abcdef7'))

# 4. Write a function that uses a regex expression to return a list of all the instances of dog or dogs.
# Exmaple:
# Input: 'Hey dog, how are you dog, where are all the dogs? Man these dogs are lost dog on it.'
# Output: ['dog', 'dog', 'dogs', 'dogs', 'dog']

def findStrs(str):
    regEx = r'dog[s]?'
    match = re.findall(regEx, str)

    return match

# print(findStrs('Hey dog, how are you dog, where are all the dogs? Man these dogs are lost dog on it.'))

# 5. Write a function that uses a regex expression to return a list that only includes the numbers.
# Exmaple:
# Input: 'Ten 10, Twenty 20, Thirty 30'
# Output: ['10', '20', '30']

def onlyNums(str):
    regEx = r'\d+'
    match = re.findall(regEx, str)

    return match

# print(onlyNums('Ten 10, Twenty 20, Thirty 30'))


# 6. Write a function that uses a regex expression to return a list with all the words that start with 'a' or 'e'.
# Exmaple:
# Input: 'The following example creates an array list with 50 elements.'
# Output: ['example', 'an', 'array', 'elements']

def aOrE(str):
    regEx = r'\b[aeAE]\S*'
    match = re.findall(regEx, str)

    return match

# print(aOrE('The following example creates an array list with 50 elements.'))

# 7. Write a function that uses a regex expression to abbreviate 'Road' as 'Rd.' in a given string.
# Exmaple:
# Input: '21 Rainbow Road'
# Output: '21 Rainbow Rd.'

def road(str):
    regEx = r'Road'
    match = re.sub(regEx, 'Rd.', str)

    return match

# print(road('21 Rainbow Road'))

# 8. Write a function that uses a regex expression to replace all occurrences of space, comma, or period with a colon.
# Exmaple:
# Input: 'Python Exercises, PHP exercises.'
# Output: 'Python:Exercises::PHP:exercises:'

def colonsOnly(str):
    regEx = r'[\s\,\.]'
    match = re.sub(regEx, ':', str)

    return match

# print(colonsOnly('Python Exercises, PHP exercises.'))

# 9. Write a function that uses a regex expression to return a list of all words in a string that are exactly five characters long.
# Exmaple:
# Input: 'The quick brown fox jumps over the lazy dog.'
# Output: ['quick', 'brown', 'jumps']

def fiveCharacterLimit(str):
    regEx = r'\S{5}'
    match = re.findall(regEx, str)

    return match

# print(fiveCharacterLimit('The quick brown fox jumps over the lazy dog.'))



# 10. Write a function that uses a regex expression to return a string that has all extra spaces removed. One space between words should be kept, but any extra spaces should be removed.
# Exmaple:
# Input: 'Python      Exercises'
# Output: 'Python Exercises'

def lessSpace(str):
    regEx = r'\s+'
    match = re.sub(regEx, ' ', str)

    return match

# print(lessSpace('Python      Exercises'))

# 11. Write a function that uses a regex expression to return a string with all non-alphanumeric characters removed.
# Exmaple:
# Input: '**//Python Exercises// - 12. '
# Output: 'PythonExercises12'

def removeNonAlphas(str):
    regEx = r'[^\w\d]'
    match = re.sub(regEx, '', str)

    return match

# print(removeNonAlphas('**//Python Exercises// - 12. '))

# 12. Write a function that uses a regex expression to return a list of words that was split by capital letters.
# Exmaple:
# Input: 'PythonTutorialAndExercises'
# Output: ['Python', 'Tutorial', 'And', 'Exercises']

def splitCaps(str):
    regEx = r'[A-Z][a-z]*'
    match = re.findall(regEx, str)

    return match

# print(splitCaps('PythonTutorialAndExercises'))

# 13. Write a function that uses a regex expression to return the following string replacement that is case-insensitive.
# Exmaple:
# Input: 'Hello HOTDOG, how are you? Do you even like hotdogs?'
# Output: 'Hello CUPCAKE, how are you? Do you even like cupcakes?'

def replaceHotdogs(string_input):
    regEx = r'(hotdogs)'
    regEx2 = r'hotdog'
    match = re.sub(regEx, 'cupcakes', string_input, flags=re.I)
    match2 = re.sub(regEx2, 'CUPCAKE', str(match), flags=re.I)

    return match2

# print(replaceHotdogs('Hello HOTDOG, how are you? Do you even like hotdogs?'))


# 14. Write a function that uses a regex expression to return a string that has all words that are between 1 and 3 characters removed.
# Exmaple:
# Input: 'The quick brown fox jumps over the lazy dog.'
# Output: 'quick brown jumps over lazy.'

def onlyMoreThanThree(string_input):
    regEx = r'\b\s?[\w]{1,3}\b'
    match = re.sub(regEx, '', string_input)

    return match

# print(onlyMoreThanThree('The quick brown fox jumps over the lazy dog.'))

# 15. Write a function that uses a regex expression to return a list of strings who's parenthesis section has been removed.
# Exmaple:
# Input: ['example (.com)', 'w3resource', 'github (.com)', 'stackoverflow (.com)']
# Output: ['example', 'w3resource', 'github', 'stackoverflow']



# 16. Write a function that uses a regex expression to return a string with all the lowercase letters removed.
# Exmaple:
# Input: 'KDeoALOklOOHserfLoAJSIskdsf'
# Output: 'KDALOOOHLAJSI'



# 17. Write a function that uses a regex expression to return the boolean True if the string passed in has an 'a' followed by two or three 'b's. Otherwise return False.
# Exmaple:
# Input: 'ab'
# Output: False
# Input: 'aabbbbbc'
# Output: True



# 18. Write a function that uses a regex expression to return the boolean True if the string passed in has lowercase letters joined with a underscore. Otherwise return False.
# Exmaple:
# Input: 'aab_Abbbc'
# Output: False
# Input: 'aab_cbbbc'
# Output: True



# 19. Write a function that uses a regex expression to return the boolean True if the string passed in has one uppercase letter followed by lowercase letters. Otherwise return False.
# Exmaple:
# Input: 'PYTHON'
# Output: False
# Input: 'AaBbGg'
# Output: True



# 20. Write a function that uses a regex expression to return the boolean True if the string passed in has proper punctuation. Otherwise return False.
# Exmaple:
# Input: 'The quick brown fox jumps over the lazy dog'
# Output: False
# Input: 'The quick brown fox jumps over the lazy dog.' (proper punctuation can be more than just a period...)
# Output: True
