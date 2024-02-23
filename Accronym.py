words = input('Please enter words which you want the acronym of: ')

acronym = words[0]
for i in range(0, len(words) - 1):
    if words[i] == " ":
        acronym += words[i+1]

print(acronym.upper())
