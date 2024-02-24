a_list = [1, 2.3, "sand"]

# Create a set from list
a_set = set(a_list)
b_set = {1, 5, 4}

print(a_set)

# Add element to a set
a_set.add("and")

print(a_set)

# Do calculations using two sets
print(a_set.union(b_set))
print(a_set.intersection(b_set))
print(a_set.difference(b_set))
print(a_set.symmetric_difference(b_set))
