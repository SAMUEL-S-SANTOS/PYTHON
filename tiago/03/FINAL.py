#Você se formou e conseguiu um emprego. Agora quer comprar uma casa. Para isso, irá economizar 
# uma porcentagem de seu salário todo mês e colocar em uma caderneta de poupança.

#Faça um programa que pergunta para o usuário:

#1) Qual o seu salário.
#2) Qual a porcentagem que ele deseja economizar todo mês.
#3) Qual o preço da casa.

#O programa deve imprimir quantos meses de salário você deve economizar para conseguir a casa,
#assumindo que você pode comprar ela à partir do momento que conseguir pagar 25% de seu valor como 
#entrada. Assuma que a cada mês, o valor que você tinha economizado até então, rendeu 0,5% a mais 
#desde o mês anterior.

salario = float(input("Qual o seu salário?: "))
porcentagem = float(input("Qual a porcentagem que você deseja economizar todo mês?: ")) / 100    
preco_casa = float(input("Qual o preço da casa?: "))

entrada = preco_casa * 0.25
poupanca = 0    
meses = 0       
rendimento_mensal = 0.005   
valor_mensal = salario * porcentagem    
rendimento = 0

while poupanca < entrada:
    poupanca += valor_mensal + rendimento
    rendimento = poupanca * rendimento_mensal
    meses += 1

print("Você deve economizar por {} meses para conseguir a entrada da casa.".format(meses))  
