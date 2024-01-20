def multiply(num_1, num_2):
    if num_2 == 1:
        return num_1
    return num_1 + multiply(num_1, num_2-1)

print(multiply(7,4))