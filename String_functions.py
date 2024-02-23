string = "        This is a string    "

# Remove space at the beginning and end
print(string.strip())

# Remove space at the beginning and end then capitalize the first letter
print((string.strip()).capitalize())

# Capitalize the whole string
print(string.upper())

# Write the whole string in lowercase
print(string.lower())

# Count how many 'i's are there in the string
print(string.count("i"))

# Find where is the string "string"
print(string.find("string"))

# Replace a string by another string
print(string.replace("a", "a kind of"))

# Write elements of a list as a string separating them by different operators
a_list = ["This", "is", "me"]

print(" ".join(a_list))
print(",".join(a_list))
print(".".join(a_list))
