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
F=0
C=0


# cálculos
C = float(input('Digite a temperatura: '))


# cálculos
F = (9 * C + 160) / 5

# exibindo resultados na tela
print('A temperatura em Fahrenheit é: ', F )
print('\n') # pula uma linha
time.sleep(5) # pausa de  5 segundos
sys.exit # comando de fim do programa
