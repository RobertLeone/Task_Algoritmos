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
SEXO = ""
MSG = ""

# Ler variável
SEXO = input('Digite o sexo: ')

#Lógica IF

if SEXO == "F":
    MSG = "uma mulher!"
else:
    MSG = "um homem!"

# sem cálculos

# exibindo resultados na tela
print('Você é', MSG )
print('\n') # pula uma linha
time.sleep(5) # pausa de  5 segundos
sys.exit # comando de fim do programa