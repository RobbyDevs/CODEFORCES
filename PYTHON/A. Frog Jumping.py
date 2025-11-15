for w in range(int(input())):
    
    a,b,k = map(int,input().split())
    
    e = d = k//2
    
    if k %2 !=0:
        d +=1
        
    e = e*b
    d = d * a
    print(d-e)