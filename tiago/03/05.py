#Escreva um programa que:

#1) Salva um número secreto em uma variável
#2) Pede para o usuário adivinhar o número
#3) Imprime 'True' ou 'False' dependendo do usuário ter adivinhado corretamente ou não.
#4) Se o usuário errou, o programa deve avisar se o número correto é maior ou menor que o número dito pelo usuário.

from random import randint

numero = randint(1,10)
advinhar = int

while advinhar != numero: 
   advinhar = int(input("advinhe o numero(1-10): "))   
   if advinhar > 10 or advinhar < 1:
         print ("ERROR")
         break
   if advinhar == numero:
      print("True")
   else:
    print("False")
    if advinhar > numero:
       print("numero que você escolheu é maior que o numero correto")
    elif advinhar < numero:
       print("numero que você escolheu é menor que o numero correto")
       
    
    
     
   
   

