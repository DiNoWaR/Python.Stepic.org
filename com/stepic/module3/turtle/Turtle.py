number = int(input())
command_array = []

result_array = [0, 0]

while number > 0:
    command = input().split(" ")
    command_array.append(command)
    number -= 1

for command in command_array:
    command[1] = int(command[1])

for command in command_array:
    if command[0] == "север":
        result_array[1] += command[1]
    elif command[0] == "юг":
        result_array[1] -= command[1]
    elif command[0] == "запад":
        result_array[0] -= command[1]
    elif command[0] == "восток":
        result_array[0] += command[1]

print(result_array[0], result_array[1], sep=' ')
