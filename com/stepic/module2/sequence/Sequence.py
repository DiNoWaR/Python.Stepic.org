number = int(input())
sequence = []
counter = 1


def create_array(item):
    array = []

    i = 0

    while i < item:
        array.append(item)
        i += 1

    return array


while counter <= number:
    array = create_array(counter)
    sequence = sequence + array
    counter += 1

counter = 0

while counter < number:
    print(sequence[counter])
    counter += 1
