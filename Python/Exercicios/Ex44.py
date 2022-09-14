#Entrar via teclado com dez valores positivos. Consistir a digitação e enviar mensagem de erro, se necessário. Após a digitação, exibir: a) O maior valor; b) A soma dos valores; c) A média aritmética dos valores;
 
s=0
maior = 0
for i in range (1, 11, 1):
    a = int(input("Digite um valor positivo: "))
    while (a<0):
        a = int(input("Valor inválido! Digite um valor positivo: "))
if (i == 1):
    maior = a
    s = s + a
while (i>1):
    if (maior > a):
        maior = a
s = s + a
media = s/10

print(f"O maior valor digitado é: {maior}")
print(f"A soma dos valores digitados é {s} ")
print(f"A média dos valores digitados é {media}")



