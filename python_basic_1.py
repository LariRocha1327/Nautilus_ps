
'''
CRIE UMA FUNÇÃO QUE REALIZE TANTO UMA PA  QUANTO UMA PG PARA VALORES INTEIROS SE 
A RAZÃO FOR PAR DEVERÁ SER REALIZADA UMA P.A DE TERMO N1 ATÉ UM VALOR X QUE NÃO 
DEVE SER ULTRAPASSADO SE O VALOR DA RAZÃO FOR ÍMPAR A FUNÇÃO REALIZARA UMA PG

cada termo tanto da PA quanto da PG devem ser armazenados em uma lista 
'''

import math
                              
lista=[]

n1=int(input ("entre com o valor do primeiro termo: "))
nx=int(input ("entre com o valor do ultimo termo:  "))
r=int(input ("entre com o valor da razão entre os numeros: "))

if r%2==0:
    continua=True
    valor_atual=n1

    while continua==True:

        if valor_atual<=nx:
            lista.append(valor_atual)
            valor_atual+=r
        else:
            continua=False
    print(lista)

else:
    
        continua=True
        valor_atual=n1
        while continua==True:

            if valor_atual<=nx:
                lista.append(valor_atual)
                valor_atual*=r
            else:
                continua=False
        print(n1, lista)