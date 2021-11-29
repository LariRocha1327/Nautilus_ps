'''
Implemente um modelo que razoavelmente descreva o problema abaixo, empregando OO. 
Garanta que existam métodos que permitam que todas as operações descritas sejam possíveis.
Imagine que você está desenvolvento uma aplicação que exibe a tabela de um campeonato qualquer. 
Cada time deve ter um nome, uma pontuação e no minimo 4 campos de sua escolha, 
que sejam relevantes a competição.ok

Requerimentos:
Cada participante/time deve ser um objeto instanciado 

Os times devem ser comparados e ordenados por numero de pontos 

Ao printar um desses objetos, o usuário deve receber informações relevantes 

Ao somar ou subtrair times devemos receber a soma ou diferença dos seus pontos. 
'''
import math

class Time:
    def __init__(self, nome, pontos, num_jogadores, num_vitorias, num_derrotas, gols_sofridos):
        self.nome = nome 
        self.pontos = pontos
        self.num_jogadores = num_jogadores
        self.num_vitorias = num_vitorias
        self.num_derrotas = num_derrotas
        self.gols_sofridos = gols_sofridos

    def Apresentar (self):
        print(f"O time do {self.nome} tem {self.pontos} pontos, e {self.num_vitorias} vitorias")

    
   
times = []
times.append(Time("Brazil", 20, 7, 10, 11, 7))
times.append(Time("Japao", 27, 7, 13, 9, 5))
times.append(Time("Canada", 15, 7, 6, 13, 11))

for i in range(len(times)):
    for y in range(len(times) - 1):
        if times[i].pontos >times[y].pontos:
            times[i], times[y] = times[y], times[i]


for time in times:
    time.Apresentar()
