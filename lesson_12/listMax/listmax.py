def list_max(list, max=0, index=0):
    if index == len(list)-1:
        return max
    if list[index] > list[index+1]:
        max = list[index]
    return list_max(list, max, index+1)

print(list_max([1,3,5,6,4]))