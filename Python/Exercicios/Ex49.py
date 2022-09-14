#Crie um programa que solicite que o usuário entre com dois números (inicial e final). Ao final o programa deverá apresentar o valor total da soma de todos os números do intervalo digitado pelo usuário.

a = int(input("Digite um valor inicial: "))
b = int(input("Digite um valor final: "))

for i in range (a, b, 1):
    s = a + i
    print(f" {s}")
