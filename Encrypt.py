message = input('Enter a message: ')
shift = int(input('How many character should we shift (1-26): '))

new_message = ""
old_message = ""
num = 0

# To encrypt the message
for char in message:
    check = char.isalpha()
    if check:
        num = ord(char) + shift
        num = chr(num)
        new_message += num
    else:
        new_message += char

# To decrypt the message
for char in new_message:
    check = char.isalpha()
    if check:
        num = ord(char) - shift
        num = chr(num)
        old_message += num
    else:
        old_message += char
      
print("Encrypted: ", new_message)
print("Decrypted: ", old_message)
