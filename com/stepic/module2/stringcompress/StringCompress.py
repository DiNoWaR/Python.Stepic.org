genom = input()

i = 0

result = ''
counter = 1

while i <= (len(genom) - 1):

    current = genom[i]

    if len(genom) == 1:
        print(current + str(1))
        break
    else:
        if genom[i + 1] == current:
            counter += 1
            if i == len(genom) - 2:
                result += current + str(counter)
                break
        else:
            if i == len(genom) - 2:
                result += current + str(counter)
                counter = 1
                current = genom[i + 1]
                result += current + str(counter)
                break
            else:
                result += current + str(counter)
                counter = 1

        i += 1

print(result)
