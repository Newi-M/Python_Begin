# Go through numbers 1 to 10
for num in range(1, 11):

    # Check if each number is even or odd and print which category it is included in
    if (num % 2) == 0:
        print("{} is Even".format(num))
    else:
        print("{} is Odd".format(num))
