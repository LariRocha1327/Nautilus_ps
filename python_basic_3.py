'''
o Reino Unido, a moeda é composta por libra (£) e pence (p). 
Existem oito moedas em circulação geral:

1p, 2p, 5p, 10p, 20p, 50p, £ 1 (100p) e £ 2 (200p).
É possível ganhar £ 2 da seguinte maneira:

1 × £ 1 + 1 × 50p + 2 × 20p + 1 × 5p + 1 × 2p + 3 × 1p
De quantas maneiras diferentes £ 2 podem ser feitas usando qualquer número de moedas?

'''
'''
formula 
(1-x)(1-x^5)(1-x^10)(1-x25)(1-x^50)(1-x^100)
'''
x=2
som=((1-x)*(1-x^2)*(1-x^5)*(1-x^10)*(1-x^20)*(1-x^50)*(1-x^100)*(1-x^200))
print(som)