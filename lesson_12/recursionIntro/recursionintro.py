def countdown(int):
    if int == 1:
        return str(int)
    return (str(int) + ', '+countdown(int-1))

def countup(int):
    if int == 1:
        return str(int)
    return (countup(int-1) + ', ' + str(int))

def sum_countup(int):
    if int == 1:
        return int
    return int + sum_countup(int-1)



print(countdown(5))
print(countup(5))
print(sum_countup(5))