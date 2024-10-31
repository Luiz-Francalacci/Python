#1
numero:int
lista = []
for x in range(0,6):
    numero = int(input("Digite o numero"))
    lista.append(numero)
print(lista)

#2
A = [1, 0, 5, -2, -5, 7]
soma = A[0] + A[1] + A[5]
print(soma)
A[5] = 100
print(A)
for x in A:
    print(x)

#3
lista1 = []
for x in range(10):
    lista1.append(int(input("Digite o numero")))
print(lista1)
for x in lista1:
    if x%2 == 0:
        print(x)



