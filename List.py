a_list = ["string", 1, 1.2, "c"]

b_list = list(range(10))

print(a_list)
print(b_list)

# Concatenate lists
c_list = a_list + b_list

print(c_list)

# Print list twice
print(a_list[0] * 2)

# Length of list
print(len(a_list))

# Check if element in a list
print(1 in a_list)

for i in a_list:
    print("{}:{}".format(a_list.index(i), i))
