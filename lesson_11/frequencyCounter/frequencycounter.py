def same(list_1, list_2):
    if len(list_1) != len(list_2):
        return False
    count_1 = {}
    count_2 = {}
    for num in list_1:
        if num in count_1:
            count_1[num] += 1
        else:
            count_1[num] = 0
    for num in list_2:
        if num in count_2:
            count_2[num] += 1
        else:
            count_2[num] = 0
    for key in count_1:
        if (key**2) not in count_2:
            return False
        if count_1[key] != count_2[key**2]:
            return False
    return True


# Test Cases
print(same([1, 2, 3], [4, 1, 9])) # true
print(same([1, 2, 3], [1, 9])) # false
print(same([1, 2, 1], [4, 4, 1])) # false (must be same frequency)