source_array = [int(i) for i in input().split()]
target_array = []

length = len(source_array)

for i in range(length):
    target_array.append(i)

if length == 1:
    target_array[0] = source_array[0]

else:
    target_array[0] = source_array[1] + source_array[length - 1]
    target_array[length - 1] = source_array[length - 2] + source_array[0]

    for index, item in enumerate(source_array, 1):
        if index == length - 1:
            break
        else:
            target_array[index] = source_array[index + 1] + source_array[index - 1]

for item in target_array:
    print(item)