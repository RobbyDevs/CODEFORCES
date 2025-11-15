t = int(input())    #entrada do munero de casos de teste

for ct in range(t): #para cada caso no intervalo de t...
    k = int(input())    #... entrada do tamanho da lista
    l = list(map(int, input().split())) # transforma a string em uma lista de inteiros
    conf = [0] * (k+1)  # cria uma lista nula com o mesmo numero de valores de 'l'+1
    
    k -= 2 # k sera o numero de valores reais da matriz (descontando os 2 das dimensoes da grid)
    s = []  #instancia a lista 's' com valores que multiplicados sao iguais a 'k'.

    for num in l: #para cada num na lista 'l'
        if k % num == 0:    #se a divisao de 'k' por 'num' for exata...
            if conf[num] == 0:  #... e se, na lista nula, o valor na posicao do valor 'num' for zero...
                s.append(num)     #... adicionar 'num' na lista de candidatos 's'.
            conf[num] += 1  #posicao do valor 'num' incrementa em 1
            # condicao de controle para verificar posterior mente se havera valores candidatos repetidos
    
    for v in s:     #para cada v na lista de candidatos...
        o = k//v    #o recebe div inteira de k por v

        if o == v and conf[o] > 1: # se 'o' for igual a 'v' e houver mais de um valor iguala a 'o' na lista...
            print(o, v) #imprimir (o v)
            break  #interrupçao do caso de teste

        elif o != v and conf[o] >= 1:#  ... se não, se 'o' for diferente de 'v' e houver um ou mais valores iguais a 'o' na lista...
            print(o, v) #imprimir (o v)
            break  #interrupçao do caso de teste
            