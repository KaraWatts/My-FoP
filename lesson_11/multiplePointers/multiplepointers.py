def sumZero(list):
    for index, num in enumerate(list):
        if num*(-1) in list and list[index] != num*(-1):
            return [num,num*(-1)]
    return -1

#Bad solution O(n^2) due to search within the if statement

        
# Test Cases
print(sumZero([-3, -2, -1, 0, 1, 2, 3])) # [-3, 3]
print(sumZero([-10, -5, 0, 1, 3, 5, 87, 99])) # [-5, 5]
print(sumZero([-2, 0, 1, 3])) # -1
print(sumZero([1, 2, 3])) # -1
