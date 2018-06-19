mapa = {'apple': 'fruit'}

mapa.update({'tomato': 'vegetable'})

mapa['cucumber'] = 'vegetable'

for key, value in mapa.items():
    print(key, value)
