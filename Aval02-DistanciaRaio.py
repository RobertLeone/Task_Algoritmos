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
D = 0
T = 0

# Ler variável
T = int(input('Digite o numero da base: '))

# cálculos
D = T*340

# exibindo resultados na tela
print('Distância do raio é: ', D, 'Metros' )
print('\n') # pula uma linha
time.sleep(5) # pausa de  5 segundos
sys.exit # comando de fim do programa