"""Faça um algoritmo (encapsulado em uma função)  que leia um salário de um funcionário e o aumente 
em 15%. Após o aumento, desconte 5% de impostos. Imprima o salário inicial, o salário com o aumento 
e o salário final.

Use as seguintes funções:

def calcula_aumento(v):
        ENTRADA: Um valor numérico 'v' representando um salário.
         SAÍDA:  O valor inicial 'v' após passar por um aumento de 15% 

def calcula_desconto(v):
         ENTRADA: Um valor numérico 'v' representando um salário.
         SAÍDA:  O valor inicial 'v' após passar por um desconto de 8% de impostos

def calcula_salario_final(v):
        ENTRADA: Um valor numérico 'v' representando um salário.
         SAÍDA:  O valor inicial 'v' após passar por todos os  descontos e aumentos previstos"""


def calcula_aumento(v):
    auemnto = v * 0.15
    return v + auemnto

def calcula_desconto(v):
 return v - (v * 0.08)


def calcula_salario_final(v):
 salario_com_aumento = calcula_aumento(v)
 return calcula_desconto(salario_com_aumento)



salario = float(input("qual é o seu salario: "))
salario_aumento = calcula_aumento(salario)
salario_final = calcula_salario_final(salario)

print(f"seu salario inicial é: R$ {salario:.2f}")
print(f"seu salario com aumento é: R$ {salario_aumento:.2f}")
print(f"seu salario final é: R$ {salario_final:.2f}")







