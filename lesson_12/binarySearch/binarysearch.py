def binarySearch(list, value):
    left = 0
    right = len(list)-1
    while left <= right:
        middle = (left + right) // 2
        print(middle)
        if list[middle] == value:
            return middle
        elif list[middle] < value:
            left = middle + 1
        elif list[middle] > value:
            right = middle -1
    return -1

# Test Cases
print(binarySearch([5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 40, 44, 64, 79, 84, 86, 95, 96, 98, 99], 10)) # 2
print(binarySearch([5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 40, 44, 64, 79, 84, 86, 95, 96, 98, 99], 95)) # 16
print(binarySearch([5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 40, 44, 64, 79, 84, 86, 95, 96, 98, 99], 100)) # -1
