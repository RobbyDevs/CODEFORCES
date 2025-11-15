for w in range(int(input())):
    
    n = int(input())
    
    a = n**(1/2)
    
    if a - int(a) == 0:
        print(int(a),'0')
    else:
        print(-1)