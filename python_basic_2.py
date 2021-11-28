
'''
    Escreva uma função que recebe um inteiro como entrada e retorna o número 
    de bits que são iguais ao numero binário representação desse número. 
    Você pode garantir que a entrada não é negativa.

    Exemplo: a representação binária de 1234 é 10011010010, então a função deve 
    retornar 5 neste caso
'''

import math

n=int(input ("entre com um numero inteiro positivo: "))

if n>=0:
    binario=bin(n) [2:]
    print(binario)
else:
    print("Apenas numeros inteiros positivo!")

bin1=[int(i)for i in str(binario)]
bit=bin1.count(1)
print(bit)