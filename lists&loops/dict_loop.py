# Looping over a dictionary

# student_grades = {"John": 6.5, 
#                   "Will":4.5,
#                   "Josh":7.8}

# for grades in student_grades.values():  # change grades.values to grades.keys for keys and same for the whole item (grade.items)
#         print(grades)


# json_loads = {'buildNumber': '1',
#               'status':'completed',
#               'result':'succeeded'
# }

# for json in json_loads.values():
#         print(json) 

## Get all keys of a nested dictionary

def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield from recursive_items(value)
        else:
            yield (key, value)

a = {'a': {1: {1: 2, 3: 4}, 2: {5: 6}}}

for key, value in recursive_items(a):
    print(key, value)