numbers = [1,2,3,4,5,6,7,8,9,10]

for i in range(0,len(numbers)):
    squared = numbers[i] * numbers[i]
    numbers[i] = squared

print(numbers)