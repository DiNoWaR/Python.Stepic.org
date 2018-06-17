def get_sum(first, second):
    return first + second


def append_zero(xs):
    xs.append(0)


#
get_sum(1, 3)
get_sum(second=3, first=2)

#
array = []
append_zero(array)


def get_y(x):
    if x <= -2:
        return 1 - (x + 2) * (x + 2)
    elif 2 >= x >= -2:
        return (-1 / 2) * x
    elif x > 2:
        return (x - 2) * (x - 2) + 1


def modify_list(input_list):
    for i in reversed(range(len(input_list))):
        if input_list[i] % 2 != 0:
            input_list.remove(input_list[i])

    for i in range(len(input_list)):
        input_list[i] = int(input_list[i] / 2)


array = [1, 3, 5, 7]
modify_list(array)
