inf = open('dataset.txt')
input_string = inf.readline().strip()
inf.close()

letter = ''
temp_array = []

result_array = []
result_string = ''


def create_number_from_array(array):
    result = ''

    if len(array) == 0:
        return 0

    for item in array:
        result += item

    return int(result)


for index, item in enumerate(input_string):
    if not item.isdigit():
        letter = item
    else:
        temp_array.append(item)

        if index == len(input_string) - 1:
            result_array.append(create_number_from_array(temp_array) * letter)
            temp_array.clear()
            break

        if not input_string[index + 1].isdigit():
            result_array.append(create_number_from_array(temp_array) * letter)
            temp_array.clear()

for item in result_array:
    result_string += item

ouf = open('result.txt', 'w')
ouf.write(result_string + '\n')
ouf.close()
