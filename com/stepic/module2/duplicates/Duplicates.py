source_array = [int(i) for i in input().split()]
sorted_array = sorted(source_array)

target_array = []

counter = 0

length = len(source_array)

for (index, item) in enumerate(sorted_array):
    if index == length - 1:
        break
    else:
        if sorted_array[index] == sorted_array[index + 1]:

            if counter == 0:
                counter = counter + 1
                target_array.append(item)

        else:
            counter = 0


for item in target_array:
    print(item)
