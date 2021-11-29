'''
A série, 11 + 22 + 33 + ... + 1010 = 10405071317.

Encontre os últimos dez dígitos da série, 1 ^ 1 + 2 ^ 2 + 3 ^ 3 + ... + 1000 ^ 1000.
'''

cont = 0
for i in range(1000):
    cont += i**i
    
cont1=str(cont)
print(cont1 [-10:])
    
