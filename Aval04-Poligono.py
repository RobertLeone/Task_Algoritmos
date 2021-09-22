# Configura o idioma em Português
# -*- coding: utf-8 -*-

#usando módulos do python
import os
import sys
import time
import math

# Apagar a tela
os.system('cls')
print('\n')

# Variáveis e constantes
NL = 0
NL1 = 0
ML = 0
P = 0
C = 0
M = ""

# Ler variável
NL = input('Digite o tamanho dos lados: ').split(" ")
ML = len(NL) #Quantidde de lados
NL1 = list(map(int, NL))

# Lógica IF
if ML == 3:
    P = (NL1[0] + NL1[1] + NL1[2]) / 2
    C = (P*(P - NL1[0])*(P - NL1[1])*(P - NL1[2])) ** (1/2)
    M = "TRIÂNGULO"
elif ML == 4:
    C = NL1[0] + NL1[1] + NL1[2] + NL1[3]
    M = "QUADRADO"
elif ML == 5:
    C = (5*(NL1[0]**2)) / (4*math.tan(math.radians(36)))
    M = "PENTAGONO REGULAR"
elif ML > 5:
    print("Polígono não identificado")
    exit()
else:
    print("Não é um polígono")
    exit()
# Sem cálculos

# Exibindo resultados na tela
print(f"O polígono é um: {M}\n"
      f"Sua área é de: {C:.2f}")
print('\n') # pula uma linha
time.sleep(5) # pausa de  5 segundos
sys.exit # comando de fim do programa