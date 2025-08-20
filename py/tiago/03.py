def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primeiros_primos(qtd=100):
    primos = []
    num = 2
    while len(primos) < qtd: 
        if eh_primo(num):
            primos.append(num)
        num += 1
    return primos

print(primeiros_primos(100))