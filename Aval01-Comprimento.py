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
Vl = 0
C = 0
L = 0
H = 0


# cálculos
C = float(input('Digite o comprimento: '))
L = float(input('Digite a largura: '))
H = float(input('Digite a altura: '))


# cálculos
Vl = C * L * H

# exibindo resultados na tela
print('O volume é: ', Vl )
print('\n') # pula uma linha
time.sleep(5) # pausa de  5 segundos
sys.exit # comando de fim do programa
