class OutOfRangeError(Exception):
    pass

def nameTheNumber():
    try:
        number = int(input('Enter a number (1, 2, or 3): '))

        if number == 1:
            print("one")
        elif number == 2:
            print('two')
        elif number == 3:
            print('three')
        else:
            raise OutOfRangeError("That's not one of the allowed values")
    except ValueError:
        print("Invalid input, please enter a number value")
    except OutOfRangeError as i:
        print(f'That is not one of the allowed values!')
        
try:
    nameTheNumber()
except:
    print('fail')