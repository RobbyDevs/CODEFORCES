for w in range(int(input())):
    
    n = int(input())
    
    v = []
    for i in range(1,n+1):
        aa,bb = map(int,input().split())
        if aa >10:
            v.append(0)
        else:
            v.append(bb)
            
        
    print(v.index(max(v))+1)