genom = input()

count = 0

for item in genom:
    if item.lower() == 'g' or item.lower() == 'c':
        count += 1

print((count / len(genom) * 100))


