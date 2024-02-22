# Assign a secret number which the user is going to guess
secret_no = 3

# Ask the user to guess a number 1 to 10
num = int(input('Guess a number from 1 to 10: '))

if num != secret_no:
    while num != secret_no:
        if num < secret_no:
            num = int(input('Too low! Enter another number: '))
        else:
            num = int(input('Too high! Enter another number: '))

print('Your guess is correct!')
