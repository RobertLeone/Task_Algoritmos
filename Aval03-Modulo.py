# Configura o idioma em Português
# -*- coding: utf-8 -*-

#usando módulos do python
import os
import sys
import time

# apagar a tela
os.system('cls')
print('\n')

# variáveis e constantes
A = 0


# Ler variável
A = int(input('Digite o valor: '))

#Lógica IF

if A > 0:
    M = A
else:
    M = A * -1

# sem cálculos

# exibindo resultados na tela
print(f'O valor em módulo é: {M}')
print('\n') # pula uma linha
time.sleep(5) # pausa de  5 segundos
sys.exit # comando de fim do programa
