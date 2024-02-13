# Accept age as an input and convert it to an integer
age = int(input('Enter your age: '))

# Print different information based on the age
if age <= 5:
    print('Go to kindergarten.')
elif (age >= 6) and (age <= 18):
    print('Go to grades 1 to 12.')
else:
    print('Go to college.')
