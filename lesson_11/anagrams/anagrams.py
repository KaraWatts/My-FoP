def validAnagram(list_1, list_2):
    if len(list_1) != len(list_2):
        return False
    count_1 = {}
    count_2 = {}
    for char in list_1:
        if char in count_1:
            count_1[char] += 1
        else:
            count_1[char] = 0
    for char in list_2:
        if char in count_2:
            count_2[char] += 1
        else:
            count_2[char] = 0
    for key in count_1:
        if key not in count_2:
            return False
        if count_1[key] != count_2[key]:
            return False
    return True

# Test Cases
print(validAnagram('aaz', 'zza')) # false
print(validAnagram('anagram', 'nagaram')) # true
print(validAnagram('rat', 'car')) # false
print(validAnagram('qwerty', 'qeywrt')) # true
