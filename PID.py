
erro=30
erro_pas=0 #erro passado
erro_pas_aculm=0 #acumulação de erros passados

kp=3
ki=1
kd=0.1

for i in range(10):

    erro_derivativo= erro-erro_pas #recebe o valor de erro e erro passado começando em 0

    print(erro_derivativo)
    print(erro_pas)

    erro_pas_aculm+=erro_pas #erro acumulado recebe o valor atual dele mais o(s) erro(s) passado(s)
    print(erro_pas_aculm)

    erro_pas=erro #erro passado recebe o valor do erro atual para o proximo loop
    print(erro_pas)

    erro_intg=erro+(erro_pas_aculm)
    print(erro_intg)

    pid=kp*erro+kd*erro_derivativo+ki*erro_intg
    erro=pid
    

print(erro)
