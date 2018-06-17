array = [int(i) for i in input().split()]

minimum = array[0]

for i in array:
    print(i)

for item in array:
    if item < minimum:
        minimum = item

print(minimum)


