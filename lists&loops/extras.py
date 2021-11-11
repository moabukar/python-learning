import copy


# list and adding to list

def eggs(somenumber):
    somenumber.append('Hello')

spam = [1,2,3]
eggs(spam)
print(spam)

# using copy (deepcopy) library to copy lists to new lists

import copy

cheese = copy.deepcopy(spam)
eggs(cheese)
print(cheese)