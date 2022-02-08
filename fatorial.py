#################################################################
# Finalidade: Consiste em receber um número natural e mostrar o #
# seu resultado fatorial.                                       #
# Nome:	fatorial.py                 							#
# Autor: Bruno Souza                							#
# Data Criação: 02/02/2022          							#
#################################################################
n = int(input("Digite o valor de n: "))
fact = n



if fact == 1 or fact == 0:
    print("1")
elif fact < 0:
    print("Por favor, digite um número natural.")
if n > 1:
    while n > 1:
        n = n - 1
        fact = fact * n
    print(fact)

