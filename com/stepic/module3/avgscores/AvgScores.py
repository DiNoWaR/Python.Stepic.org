def reduce(array):
    sum = 0

    for item in array:
        sum += item

    result = sum / len(array)
    return result


lines = [line.rstrip('\n') for line in open('dataset.txt')]

input_array = []

for line in lines:
    temp_array = line.split()
    input_array.append(temp_array)

source_map = {}

for item in input_array:
    if item[0] not in source_map:
        source_map[item[0]] = [int(item[2])]
    else:
        source_map[item[0]].append(int(item[2]))

for key, value in source_map.items():
    avg_score = reduce(value)
    source_map[key] = avg_score

target_array = []

for i in range(1, 12):
    if str(i) in source_map:
        target_array.append([i, source_map[str(i)]])
    else:
        target_array.append([i, "-"])

ouf = open('result.txt', 'w')

for item in target_array:
    ouf.write(str(item[0]) + " ")
    ouf.write(str(item[1]) + "\n")

ouf.close()
