
amount = int(input(f'Please enter an amount in cents less than a dollar: '))

if 0 >= amount >= 99:
    print("This is not a valid amount")

quarters = amount // 25
amount %= 25

dimes = amount // 10
amount %= 10

nickles = amount // 5
pennies = amount % 5


print(f'Your change will be: \nQ: {quarters}\nD: {dimes}\nN: {nickles}\nP: {pennies}')