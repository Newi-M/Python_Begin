while True:

    # Try to run the following code which might cause an error
    try:
        num = int(input('Please enter a number'))
        
        # If num is successfully converted to integer, then break the loop
        break

    # Giving error message if the value entered is not an integer
    except ValueError:
        print("You haven't entered a number")
