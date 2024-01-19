def maxSubListSum(list, num):
    maxSum = 0
    temp = 0
    if num > len(list):
        return None
    for i in range(num):
        maxSum += list[i]
    temp = maxSum
    for j in range(num, len(list)):
        temp = temp - list[j-num] + list[j]
        maxSum = max(maxSum, temp)
    return maxSum


# Test Cases
print(maxSubListSum([1, 2, 5, 2, 8, 1, 5], 2)) # 10
print(maxSubListSum([1, 2, 5, 2, 8, 1, 5], 4)) # 17
print(maxSubListSum([4, 2, 1, 6], 1)) # 6
print(maxSubListSum([4, 2, 1, 6, 2], 4)) # 13
print(maxSubListSum([], 4)) # None
  
        