def add(*args):

    result = 0
    for i in args:
        result += i

    return result


print("The sum of the arguments is: ", add(2, 3, 4, 5))
