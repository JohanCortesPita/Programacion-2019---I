def mejorar_receta(pizza,topping):
    '''
    list of str -> list
    "Recibe una lista y retorna otra con su topping"

    >>> mejorar_receta(['queso', 'jamon'], 'champiñon')
    ['champiñon', 'jamon', 'queso']

    :param pizza:
    :param topping:
    :return:
    '''
    nueva_pizza = pizza.copy()
    if not (topping in pizza):
        nueva_pizza.insert(0, topping)
        return sorted(nueva_pizza)

def doble_queso(pizza):
