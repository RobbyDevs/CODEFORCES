def op(posV):
    
    global v,va,final, inicio
    
    if v[posV] == 0:
        
        if inicio>0:
            if va[inicio-1] == "?":
                va[inicio-1] = '-'
                va[inicio] = "?"
                
            else:
                va[inicio] = '-'
            
        else:
            va[inicio] = '-'
        inicio+=1
    
    if v[posV] == 1:
        #print(final,len(va)-1)
        if final<len(va)-1:
            #print("final:",va[final])
            if va[final+1] == "?":
                #print("SIM")
                va[final+1] = '-'
                va[final] = '?'
            else:
                va[final] = '-'
        else:
            va[final] = '-'
        
        final-=1
        
    if v[posV] == 2:
        
        if inicio>0:
            if va[inicio-1] == "?":
                va[inicio-1] = '-'
                va[inicio] = "?"
                inicio+=1
                return
                
        if final<len(va)-1:
            #print("final:",va[final])
            if va[final+1] == "?":
                #print("SIM")
                va[final+1] = '-'
                va[final] = '?'
                final+=1
                return
        
        
        va[inicio] = "?"
        va[final] = "?"
        inicio +=1
        final-=1
        
            



for w in range(int(input())):
    n,k = map(int,input().split())
    
    global va
    va = ["+" for x in range(n)]
    
    global v
    v = [int(x) for x in input()]
    global final, inicio
    
    final = n-1
    inicio = 0
    meio = 100000000009
    if n%2:
        meio = (n//2)
    #print(meio)
    ant = 3
    for i in range(k):
        op(i)
        ant = v[i]
        
    print(*va,sep="")
            