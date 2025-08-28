'''''
Escreva uma função que satisfaz a seguinte especificação:

def conta_numeros_com_raiz_perto_de(n, epsilon):
    """
    ENTRADA: 'n' é um inteiro maior que 2
                       'epsilon' é um inteiro positivo  menor que 1
    SAÍDA: Retorna quantos números inteiros tem uma raíz quadrada próxima de 'n'.
                 Uma raíz quadrada próxima é aquela que tem uma distância menor que 'epsilon' do valor 'n'.
    """

# DICA: Calcular a raíz quadrada é a mesma coisa que elevar à (1/2), ou 0.5.
# EXEMPLO: print(conta_numeros_com_raiz_perto_de(10, 0.1)) deve imprimir 4, pois os seguintes números tem raíz quadrada próxima:
#     * 99 (a raíz é 9.9498743710662)
#     * 100 (a raíz é 10)
#     * 101 (a raíz é 10.04987562112089)
#     * 102 (a raíz é 10.099504938362077)

'''