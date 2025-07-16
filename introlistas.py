#Declaracion listas
nombres = ['Juan', 'Ana', 'Pedro', 'Maria']
# print(nombres[0])  # Imprime el primer elemento de la lista
# for nombre in nombres:
#     print(nombre)  # Imprime cada nombre en la lista

# nombres.append('Luis')  # Añade un nuevo nombre al final de la lista
# nombres.append(input("Introduce un nombre: "))  # Añade un nombre introducido por el usuario
nombres.insert(-2, 'Ana')  # Inserta 'Carlos' en la posición 2 de la lista

# nombres.remove('Ana')  # Elimina 'Ana' de la lista
# nombres.pop(0)  # Elimina el primer elemento de la lista
# nombres.pop()  # Elimina el último elemento de la lista
# nombres.pop(-4)  # Elimina el último elemento de la lista
print(nombres.count('Ana'))  # Imprime la lista actualizada
print(len(nombres))  # Imprime la lista actualizada
for idx, nombre in enumerate(nombres):
    print(f"Idx {idx} valor {nombre}")  # Imprime el índice y el nombre
