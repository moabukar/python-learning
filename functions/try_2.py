print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats')
    else:
        print('That is not a lot of cats')
except ValueError:
    print('Not an integer type. Please input a number')

