# Write a function that uses a regex expression to return a list with all the words that start with a vowel.
# Exmaple:
# Input: 'Errors should never pass silently. Unless explicitly silenced.'
# Output: ['Errors', 'Unless', 'explicitly']
import re

string1 = 'Errors should never pass silently. Unless explicitly silenced.'
regEx = r"\b[aeiouAEIOU]\S*"
result = re.findall(regEx, string1)

print(result)



# Write another function that uses a regex expression to return a list of emails that all have the domain of gmail.com.
# Exmaple:
# Input: 'aa@xyz.com bbb@abc.com cccc@cisco.com'
# Output: ['aa@gmail.com', 'bbb@gmail.com', 'cccc@gmail.com']

