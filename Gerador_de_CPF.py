##################
# GERADOR DE CPF

from random import randint  # CRIAR NÚMEROS INTEIROS RANDÔMICOS

numero = str(
    randint(100000000, 999999999))  # CRIA NUMERAÇÃO RANDÔMICA DESDE QUE COMECE Á PARTIR DE 1 E TERMINE ATÉ NUMERO 9

novo_cpf = numero
reverso = 10
total = 0

# LOOP DO CPF

for index in range(19):
    if index > 8:
        index -= 9

    total += int(novo_cpf[index]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)

print(novo_cpf)

##################
