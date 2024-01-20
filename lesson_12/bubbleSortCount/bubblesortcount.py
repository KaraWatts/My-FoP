
def bubbleSortCount(list):
    n = len(list)
    comparisons = 0
    exchanges = 0
    for iteration in range(n):
        for index in range(0,n-1-iteration): #Subtracting iteration saves run time because it skips the already sorted values at the end of the list
            comparisons += 1
            if list[index] > list[index+1]:
                list[index], list[index+1] = list[index+1], list[index]
                exchanges += 1

    answer = (comparisons, exchanges)
    return answer

# Test Cases
print(bubbleSortCount([1, 2, 3, 5, 4, 6, 7])) # (21, 1)
print(bubbleSortCount([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) # (45, 45)
print(bubbleSortCount([2, 1, 0, 5, 4])) # (10, 4)
