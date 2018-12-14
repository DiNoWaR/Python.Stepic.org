source_array = []
target_sum = 0

while True:
    item = int(input())
    source_array.append(item)
    target_sum += item

    if target_sum == 0:
        break

target_sum = 0

for item in source_array:
    target_sum += item * item


print(target_sum)
