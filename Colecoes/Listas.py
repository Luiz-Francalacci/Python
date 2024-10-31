lista = [1,2,3,4,45,5,6,7,8,9]
lista2 = ['T', 'S', 'G']
lista3 = list(range(11))
lista4 = list("GSTEDSGGET")

print(lista3)
print(lista4)
print("\n")

if 8 in lista:
    print("tem 8")
else:
    print("nao tem 8")

if 'e' in lista2:
    print("tem e")
else:
    print("nao tem e")
print("\n")

lista2.sort()
lista.sort()

print(lista2)
print(lista)
print("\n")

print(lista4.count('E'))
print("\n")

lista.append(145)
print(lista)
lista.append([1,2,3])
print(lista)
if [1,2,3] in lista:
    print("Tem a lista")

lista.extend([55,44,33])
print(lista)

lista.insert(0, 112)
print(lista)

numero = lista.pop(4)
print(lista)
print(numero)

palavra = "Maracuja, eh a melhor fruta"
palavra = palavra.split(',')
print(palavra)
