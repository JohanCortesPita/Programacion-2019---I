Hamburguesa = ['Carne', 'Queso', 'Cebolla', 'Tomate']
pizza = ['Queso', 'Champiñon', 'Masa', 'pollo', 'carne']

combo = Hamburguesa + pizza

#print(combo)

Hamburguesa_triple = Hamburguesa * 3
print(Hamburguesa_triple)

Bebidas = ['Gaseosa', 'Jugo']

combo2 = pizza + Bebidas
print(combo2)

print('la pizza tiene carne?', 'carne' in Hamburguesa)

pizza.append('chorizo')
print(pizza)

pizza.insert(0, 'aguacate')
print(pizza)

eliminar = pizza.pop(0)
print(pizza)

pizza.remove('Masa')
print(pizza)

pizza.remove('chorizo')
print(pizza)

print