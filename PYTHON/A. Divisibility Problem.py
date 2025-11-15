for w in range(int(input())):
    
    a,b = map(int,input().split())
    
    
    
    if a %b == 0:
        print(0)
        
        
    else:
        n = a//b
        print(b*(n+1)-a)