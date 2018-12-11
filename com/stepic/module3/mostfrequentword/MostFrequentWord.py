lines = [line.rstrip('\n') for line in open('dataset.txt')]

input_array = []

for line in lines:
    temp_array = line.split()
    input_array = input_array + temp_array

target_map = {}

for word in input_array:

    lower_word = word.lower()

    if lower_word not in target_map:
        target_map[lower_word] = 1
    else:
        new_value = target_map.get(lower_word) + 1
        target_map[lower_word] = new_value

max_occur = 0
result_word = ""

for key, value in target_map.items():

    if value > max_occur:
        max_occur = value
        result_word = key

for item in input_array:
    if item.lower() == result_word:
        result_word = item
        break

ouf = open('result.txt', 'w')
ouf.write(result_word + " ")
ouf.write(str(max_occur))
ouf.close()