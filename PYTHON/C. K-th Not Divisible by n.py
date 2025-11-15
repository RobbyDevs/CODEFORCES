from math import ceil

def buscaB(n, i):
    esquerda = 1
    direita = i * n

    while esquerda < direita:
        meio = (esquerda + direita) // 2
        nao_divisores = meio - meio // n
        
        if nao_divisores < i:
            esquerda = meio + 1
        else:
            direita = meio

    return esquerda


for w in range(int(input())):
    
    n,k = map(int,input().split())
    
    print(buscaB(n,k))
    
    
# 5 8 -> 5//5 == 1

# 4-12  ->  1 2 3 - 5 6 7 - 9 10 11 - 13 14 '15'



# 3-7  ->  1 2 - 4 5 - 7 8 - '10' 11 - 13 14 - 16 17
# 1 - 21 INTERVALO
# 21/3 = 7 (n de divisores)

# 21 - 7 =  14 (n de n-divisores)


#k-esimo numero + numero de divisores de n ate kn

#n-1 * 

#2 15  ->  1 - 3 - 5 - 7 - 9 - 11 - 13 - 15 - 17 - 19 - 21 - 23 - 25 - 27 - "29" 31 33

"""
numeros de 1 a n? n-1

no i-esimo multiplo, vou ter (n-1)*i nao-divisores.


 > i -> ((n-1)*k) -1

so preciso saber quantos desses ate chegar no valor k

entao, (n-1)*k?



"""