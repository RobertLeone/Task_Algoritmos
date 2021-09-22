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
P = 0
Vl = 0
Tx = 0
Tp = 0

# cálculos
Vl = float(input('Digite o valor: '))
Tx = float(input('Digite a taxa: '))
Tp = float(input('Digite o tempo: '))

# cálculos
P = Vl + ((Vl * Tx/100)*Tp)

# exibindo resultados na tela
print('O valor da prestração é: ', P )
print('\n') # pula uma linha
time.sleep(5) # pausa de  5 segundos
sys.exit # comando de fim do programa
