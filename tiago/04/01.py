#O restaurante a quilo Bem-Bão cobra R$ 12,00 por cada quilo de refeição. Escreva um algoritmo 
#(encapsulado em uma função)  que leia o peso do prato montado pelo cliente (em quilos) e imprima o 
#valor a pagar.  Assuma que a balança já desconsidere o peso do prato.

#Implemente a função de acordo com esta especificação, e use-a para gerar o programa que imprima 
#para o usuário o valor em reais:


#def preco(p):
# """ Entrada: Um número qualquer 'p' representando o peso em quilos.
# Saída: Um inteiro representando o valor a pagar (em centavos).

def preco(p):
 
    return int(round(p * 1200))

peso = float(input("Digite o peso do prato em quilos: "))
valor_centavos = preco(peso)
valor_reais = valor_centavos / 100
print(f"Valor a pagar: R$ {valor_reais:.2f}")
