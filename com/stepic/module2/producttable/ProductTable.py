first = int(input())
second = int(input())

third = int(input())
fourth = int(input())

print(' ', end='  ')

for h_element in range(third, fourth + 1):
    print(h_element, end='  ')

print()

for v_element in range(first, second + 1):
    print(v_element, end='  ')

    for h_element in range(third, fourth + 1):
        print(h_element * v_element, end='  ')

    print()

