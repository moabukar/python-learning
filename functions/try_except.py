def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error. Divided by zero doesnt work')

print(div42by(3))
print(div42by(12))
print(div42by(7))
print(div42by(0))
