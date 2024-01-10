
def hailstone(start):
    if start.isnumeric():
        num = int(start)
        count = 0
        while num != 1:
            if num % 2 != 0:
                num = (num * 3) + 1
                count += 1
            else:
                num //= 2
                count += 1
        print(count)
    else:
        hailstone(print(f'Input invalid. Numeric values only.\n Please try again: '))


hailstone(input(f'Input starting value for hailstone: '))