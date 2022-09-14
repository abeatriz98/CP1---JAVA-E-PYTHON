#Elabore um programa que apresente os números pares maiores que 10 no intervalo fechado [A, B]. Sendo que A e B serão números inteiros escolhidos pelo usuário. Um número é par quando este satisfaz a seguinte condição: (NÚMERO mod 2 = 0)

a = int(input("Digite o valor inicial: "))
while (a<10):
    a = int(input("Valor inválido! Digite um valor maior que dez: "))
b = int(input("Digite o valor final: "))
while (b<10):
    b = int(input("Valor inválido! Digite um valor maior que dez: "))

for i in range (a, b, 1):
    if (i % 2 ==0):
        print(f"{i}")
    