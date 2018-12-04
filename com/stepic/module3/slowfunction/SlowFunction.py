number = int(input())

source_array = []
result_array = []

buffer_map = {}


def f(x):
    return x * x


for i in range(0, number):
    value = int(input())
    source_array.append(value)

for item in source_array:
    if item not in buffer_map:
        buffer_map[item] = f(item)

for item in source_array:
    result_array.append(buffer_map[item])

for item in result_array:
    print(item)