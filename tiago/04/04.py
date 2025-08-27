
def mantem_consoantes(palavra): 
   
 consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
 resultado = ""
 for caractere in palavra:
    if caractere in consoantes:
      resultado += caractere
 return resultado

#teste = input("digite uma palavra: ")
#print("{} sem vogal fica: {}".format(teste,mantem_consoantes(teste)))
print(mantem_consoantes("palavra"))