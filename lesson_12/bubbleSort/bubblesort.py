def bubbleSort(list):
    n = len(list)
    for i in range(n):
        for j in range(0,n-i-1): #array length - number of passes - 1 = the last index of the unsorted list
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

# Test Cases
print(bubbleSort([5, 3, 10, 6, 1])) # [1, 3, 5, 6, 10]
print(bubbleSort([100, 98, 101, 10])) # [10, 98, 100, 101]
print(bubbleSort([2, 1, 0, 5, 4])) # [0, 1, 2, 4, 5]
