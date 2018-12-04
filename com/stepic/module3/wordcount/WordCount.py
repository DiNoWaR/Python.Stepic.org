source_map = {}

for item in input().split():

    lower_item = item.lower()

    if lower_item not in source_map:
        source_map[lower_item] = 1
    else:
        current = source_map[lower_item]
        source_map[lower_item] = current + 1

for key, value in source_map.items():
    print(key, value)
