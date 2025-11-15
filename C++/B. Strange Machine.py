for w in range(int(input())):
    
    n,q = map(int,input().split())
    
    div = 1
    dif = 0
    v = input()
    
    for i in v:
        if i == 'A':
            div = div* 1/2
        else:
            dif =-1
            
    vv = list(map(int,input().split()))
    
    print(div)
    print(dif)
    print(dif-div)
    for valor in vv:
        
        pass
    
"""
1
6 4
BAABBA
2 8 32 95


"""