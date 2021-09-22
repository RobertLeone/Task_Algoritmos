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
F = 0
I = 0
M = ""

# Ler variável
F = input('Digite 3 valores: ').split(" ")
I = list(map(int, F))

#Lógica IF
if I[0] == I[1] or I[1] == I[2] or I[2] == I[0]:
    M = "Provavelmente você digitou valores iguais, nulos ou negativos. Tente novamente."
elif I[0] <= 0 or I[1] <= 0 or I[2] <= 0:
    M = "Provavelmente você digitou valores iguais, nulos ou negativos. Tente novamente."
else:
    M = max(I)
# sem cálculos

# exibindo resultados na tela
print(f'O valor máximo é: {M}')
print('\n') # pula uma linha
time.sleep(5) # pausa de  5 segundos
sys.exit # comando de fim do programa