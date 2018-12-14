source_array = [int(i) for i in input().split()]
index_array = []

number = int(input())

for index, value in enumerate(source_array):
    if value == number:
        index_array.append(index)

if len(index_array) == 0:
    print("Отсутствует")
else:
    for item in index_array:
        print(item)
