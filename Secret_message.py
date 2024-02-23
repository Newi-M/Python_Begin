message = input('Enter a TEXT in upper case: ')

# String to hold the ascii value of each letter of the word
secret_code = ""
for char in message:
    secret_code += str(ord(char))

print("The secret message is: ", secret_code)

# String to hold the two digits of the secret message
two_digit = ""

# String to hold the original message
original_message = ""
for num in range(0, len(secret_code) - 1, 2):
    two_digit = secret_code[num] + secret_code[num + 1]
    original_message += chr(int(two_digit))

print("Original message is: ", original_message)
