for w in range(int(input())):
    
    
    n = int(input())
    
    v = list(map(int,input().split()))
    
    
    v.sort(reverse= True)
    
    v[len(v)-1] +=1
    s = 1
    for w in v:
        s *= w
        
    print(s)