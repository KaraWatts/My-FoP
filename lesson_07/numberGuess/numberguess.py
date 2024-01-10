import random


answer = random.randrange(start=100)

count = 1
while True:
    guess = input('Guess a number: ')
    if guess.isnumeric():
        guess = int(guess)
        if guess > answer:
            print('Too high - try again')
            count += 1
            continue
        if guess < answer:
            print('Too low - try again')
            count += 1
            continue
        if guess == answer:
            print(f'You guessed it in {count} tries')
            break
    else:
        print('Not a valid guess only numbers please')


    