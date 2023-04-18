#Definindo funções em python
#Para criar funções em python, você deve usar o comando def(definition)
#seguido do nome da função e o parenteses, que pode ter ou não argumentos
#em python não é necessario definir o tipo de retorno

def soma(valores):
    x = 0
    for i in valores:
        x = x + i
    return x

def media(valores):
    x = 0
    for i in valores:
        x = x + i
    return x / len(valores)

def maior(valores):
    x = valores[0]
    for i in range(1,len(valores)):
        if(i > x):
            x = 1
    return x
