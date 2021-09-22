# Configura o idioma em Português
# -*- coding: utf-8 -*-

#usando módulos do python
import os
import sys
import time
import math

# apagar a tela
os.system('cls')
print('\n')

# variáveis e constantes
A = 0
B = 0
C = 0
M = ""

# Ler variável
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

#Lógica IF
if A >= (B+C) or B >=(A+C) or C >= (B+A):
    M = "Não é um triângulo"
elif A != B and B != C and A != C:
    M = "Triângulo Escaleno"
elif A == B and B == C and C == A:
    M = "Triângulo Equilátero"
elif A == B or B == C or C == A:
    M = "Triângulo Isósceles"

# sem cálculos

# exibindo resultados na tela
print(M)
print('\n') # pula uma linha
time.sleep(5) # pausa de  5 segundos
sys.exit # comando de fim do programa