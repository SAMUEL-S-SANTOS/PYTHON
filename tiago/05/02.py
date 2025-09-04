'''
O código abaixo tem erros. Corrija-o.
#
#  Início do código:
def eh_triangular(n):
    
    Entrada: um inteiro positivo 'n'.
    Saída: True, se 'n' é um número triangular. Isto é, ele é a soma de números naturais
                sequenciais começando em 1. Exemplo: 1+2+3+...+k
    
    total = 0
    for i in range(n):
        total += i
        if total == n:
            print(True)
    print(False)

# Você pode testar este código com alguns números para tentar achar o problema
# print(eh_triangular(4)) # Deve imprimir 'False'
# print(eh_triangular(6)) # Deve imprimir 'True'
# print(eh_triangular(1)) # Deve imprimir 'True'

'''

def eh_triangular(n):  
    if n < 0:
        return False
    soma = 0
    i = 1
    while soma < n:
        soma += i
        i += 1
    return soma == n

   

print(f"4 é triangular? {eh_triangular(4)}") 
print(f"6 é triangular? {eh_triangular(6)}") 
print(f"1 é triangular? {eh_triangular(1)}")