sample_input = list(input())
sample_output = list(input())

source_string = list(input())
cripted_string = list(input())

cript_map = dict(zip(sample_input, sample_output))

for key, value in enumerate(source_string):
    cripted_value = cript_map[value]
    source_string[key] = cripted_value

cript_map.clear()

cript_map = dict(zip(sample_output, sample_input))

for key, value in enumerate(cripted_string):
    cripted_value = cript_map[value]
    cripted_string[key] = cripted_value

for item in source_string:
    print(item, sep='', end='')

print()

for item in cripted_string:
    print(item, sep='', end='')