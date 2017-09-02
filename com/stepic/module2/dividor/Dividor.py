first = int(input())
second = int(input())

bigger = second
less = first

if first > second:
    bigger = first
    less = second

result = bigger

while True:
    if result % less == 0:
        print(result)
        break
    else:
        result += bigger
