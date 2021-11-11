# Dictionary loop with string formatting


people_numbers = {"John": "455", "Will": "345"}


for pair in people_numbers.items():
    print("{} has as number {}".format(pair[0],pair[1]))


