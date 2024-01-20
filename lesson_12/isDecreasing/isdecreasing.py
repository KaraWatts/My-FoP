def is_decreasing(list, index=0):
    if list[index] < list[index+1]:
        return False
    
    if index == len(list)-2:
        return True
    
    return is_decreasing(list,index+1)


print(is_decreasing([1,3,5,2,1]))
print(is_decreasing([1,2,3,4,5]))
print(is_decreasing([5,4,3,2,1]))
print(is_decreasing([1,2,3,3,4,5]))