# Accept two numbers as an input and store each number in a variable
num1, num2 = input('Enter two numbers separated by space: ').split()

# Convert the numbers to float
num1 = float(num1)
num2 = float(num2)

# Do calculations
result = num1 + num2
diff = num1 - num2
product = num1 * num2
quotient = num1 / num2
rem = num1 % num2

# Round the answers to two decimal place
result = round(result, 2)
diff = round(diff, 2)
product = round(product, 2)
quotient = round(quotient, 2)

# Display the answers
print('The sum of the numbers is {}'.format(result))
print('The difference of the numbers is {}'.format(diff))
print('The product of the numbers is {}'.format(product))
print('The quotient of the first number divided by the second is {}'.format(quotient))
print('The remainder of the first number divided by the second is {}'.format(rem))
