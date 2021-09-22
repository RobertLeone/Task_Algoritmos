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
Tp = 0
Vm = 0
D = 0
LS = 0

# cálculos
Tp = float(input('Digite o tempo gasto: '))
Vm = float(input('Digite a velocidade media: '))

# cálculos
D = Tp * Vm

# cálculos
LS = D / 12

# exibindo resultados na tela
print('Velocidade média: ', Vm,
      '\nTempo gasto: ', Tp,
      '\nDistância: ', D,
      '\nQuantidade de litros usados: ', LS)
print('\n') # pula uma linha
time.sleep(5) # pausa de  5 segundos
sys.exit # comando de fim do programa
