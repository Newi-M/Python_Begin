import random

rand_list = []
for i in range(5):

    # Generate random number 1 - 20
    element = random.randrange(1,21)
    rand_list.append(element)

print(rand_list)
