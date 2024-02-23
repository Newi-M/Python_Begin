string = input('Enter an equation of form x + a = b where a and b are numbers: ')


def solve():
    global string
    string = string.split()

    num1 = int(string[2])
    num2 = int(string[4])

    return num2 - num1


result = solve()
print("x = ", result)
