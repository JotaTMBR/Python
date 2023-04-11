lista1 = [2,11,3,6,4,17,10]
lista2 = [1,3,6,12,20,8]

resultado = 0
# Exibir os números pares da lista 1 e 2
# Somar ps números pares
print("\n")

for x in lista1:
    if( x % 2 == 0):
        print("Os números pares da lista1 são: "+str (x))
        resultado = resultado + x
print("\n")

for y in lista2:
    if(y % 2 == 0):
        print("Os números pares da lista2 são: "+str (y))
        resultado = resultado + y

print("\nO resultado da soma dos números pares é: "+str (resultado))