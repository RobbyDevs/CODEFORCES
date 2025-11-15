for w in range(int(input())):
    v = list(map(int,input().split()))
    v.sort()
    
    soma = abs(v[1]-v[0])+abs(v[1]-v[2])
    
    
    print(soma)