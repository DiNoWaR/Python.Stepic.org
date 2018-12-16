def create_array(size):
    array = []

    i = 0

    while i < size:
        array.append(0)
        i += 1
    return array


def fill_right(array, top_index, left_index, right_index):
    global current_value
    current_nested_array = array[top_index]

    while left_index < right_index:
        current_nested_array[left_index] = current_value + 1
        left_index += 1
        current_value += 1


def fill_down(array, top_index, right_index, down_index):
    global current_value

    while top_index < down_index:
        current_nested_array = array[top_index]
        current_nested_array[right_index] = current_value + 1
        top_index += 1
        current_value += 1


def fill_left(array, down_index, right_index, left_index):
    global current_value
    current_nested_array = array[down_index]

    while right_index >= left_index:
        current_nested_array[right_index] = current_value + 1
        right_index -= 1
        current_value += 1


def fill_up(array, down_index, left_index, top_index):
    global current_value

    while down_index >= top_index:
        current_nested_array = array[down_index]
        current_nested_array[left_index] = current_value + 1
        down_index -= 1
        current_value += 1


def generate_empty_2d_array(number):
    main_array = []

    start = 0

    while start < number:
        nested_array = create_array(number)
        main_array.append(nested_array)
        start += 1
    return main_array


number = int(input())
current_value = 0

main_array = generate_empty_2d_array(number)

i = 0

while current_value < number * number:
    fill_right(main_array, 0 + i, 0 + i, len(main_array) - i)
    fill_down(main_array, 1 + i, len(main_array) - 1 - i, len(main_array) - i)
    fill_left(main_array, len(main_array) - 1 - i, len(main_array) - 2 - i, 0 + i)
    fill_up(main_array, len(main_array) - 2 - i, 0 + i, 1 + i)
    i += 1

for item in main_array:
    print(*item)