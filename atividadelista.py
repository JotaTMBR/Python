lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# Listando intervalo de 1 a 9, e de 8 a 13
print("Lista de 1 a 9:\n")

for i in range(1,10):
    print(lista[i])

print("Lista de 8 a 13:\n")

for y in range(8,14):
    print(lista[y])

# Listando os números pares e impares

print("Lista dos números pares e ímpares:\n")

for x in lista:
    if( x % 2 == 0):
        print("Os números pares da lista são: "+str (x))
for y in lista:
    if( x % 2 != 0):
        print("Os números impares da lista são: "+str (x))

# Listando os multiplos de 2, 3 e 4

print("Multiplos de 2, 3 e 4:\n")

for m in lista:
    if( m % 2 == 0):
        print("Os multiplos de 2 são: "+str (m))
for n in lista:
    if( n % 3 == 0):
        print("Os multiplos de 3 são: "+str (n))
for o in lista:
    if( o % 4 == 0):
        print("Os multiplos de 4 são: "+str (o))

print("Lista Inversa:\n")

l = lista[::-1]
print(l)