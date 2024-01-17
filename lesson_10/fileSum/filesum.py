

num_list = [23.77, 116, 94, -12.8, 0, 14.999]

with open('num.txt', 'w') as outfile:
    for num in num_list:
        outfile.write(str(num) + '\n')

def file_sum(num_file):
    try:
        total = 0
        with open (num_file, 'r') as infile:
            for line in infile:
                total += float(line.strip())
    except FileNotFoundError:
        return 'File Not Found'

    return total

print(file_sum("num.txt"))
