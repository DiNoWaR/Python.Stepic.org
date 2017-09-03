# first, second = (int(i) for i in input().split())

first = int(input())
second = int(input())

summ = 0.0
count = 0.0

for item in range(first, second + 1):
    if item % 3 == 0:
        summ += item
        count += 1

print(summ / count)
