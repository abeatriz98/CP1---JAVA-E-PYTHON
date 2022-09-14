#Crie um programa em que o usuário entre com um número inteiro qualquer, e o programa imprima os 20 números subsequentes ao que foi digitado pelo usuário.

a = int(input("Digite um valor: "))
s = a+1

for i in range (a, 21, 1):
    print(f"{s}")
    s = s + 1 
