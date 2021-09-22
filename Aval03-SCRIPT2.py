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
media = 0
n1 = 0
n2 = 0
status = ""

# Ler variável
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

# Cálculo
media = (n1 + n2) / 2

#Lógica IF
if media < 3:
    status = 'Reprovado!'
elif media >=3 and media < 5:
    status = 'Recuperação!'
elif media >= 5 and media < 6:
    status = 'Aluno de exame!'
else:
    status = 'Aprovado!'

# exibindo resultados na tela
print(f'Sua média é: {media:.2f}')
print(f'Status: {status}')
print('\n') # pula uma linha
time.sleep(5) # pausa de  5 segundos
sys.exit # comando de fim do programa