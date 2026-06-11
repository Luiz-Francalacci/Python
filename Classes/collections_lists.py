"""Lista"""

lista = [3,2,1]
print(lista)

for x in lista:
    print(x, end =" ")
print()
lista2 = list("Abacate")
print(lista2)
lista.sort()
print(lista)
print(lista2.count("a"))


lista.append(7)
print(lista)

lista.extend([22,23,43])
print(lista)

print(lista.index(23))

