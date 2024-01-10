answer = int(input('Enter the integer for the player to guess: '))

count = 1
while True:
    guess = int(input('Guess a number: '))
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
    