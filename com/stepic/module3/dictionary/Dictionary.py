number_of_word_in_dict = int(input())
my_dict = {}

array = []

while number_of_word_in_dict > 0:
    line = input().lower()

    if line not in my_dict:
        my_dict[line] = line

    number_of_word_in_dict -= 1

number_of_lines = int(input())

while number_of_lines > 0:
    line = input().split()
    array += line
    number_of_lines -= 1

filtered_array = []

for item in array:
    if item.lower() not in my_dict:
        filtered_array.append(item)

for item in set(filtered_array):
    print(item)
