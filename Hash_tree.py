# Accept number of row as an input
row = int(input('How  tall do you want the Hash-Tree be? (Enter number of rows) '))

# Create a variable of value 1 which represent by how much the number of Hash increases in each iteration
hash_increase = 1

# Iterate printing space and hash symbol in each row
for i in range(row):

    space_no = row - (i+1)

    Hash_no = i + hash_increase
    hash_increase += 1

    j = 1
    while j <= space_no:
        print(end=" ")
        j += 1
        
    k = 1
    while k <= Hash_no:
        print("#", end="")

        if k == Hash_no:
            print()
        else:
            pass
        k += 1

    i += 1
