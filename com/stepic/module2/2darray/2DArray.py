source = []
target = []


def castToInt(array):
    for index, value in enumerate(array):
        array[index] = int(value)


while True:
    input_str = input()

    if input_str != 'end':
        array = input_str.split(" ")
        castToInt(array)
        source.append(array)
    else:
        break


for item in target:
    print(*item)
