string = "Hi"


def change_string():
    
    # Use global to show that it is the same variable as the one mentioned outside function
    global string
    string = "Hello"
    return string


print(string)
change_string()
print(string)
