for i in range(int(input())):
    n = int(input())
    
    v = list(map(int,input().split()))
    
    if n == 1:
        print(1)
        print(v[0])
        
    else:
        va = [str(v[0])]
        for i in range(1, n):
            if v[i-1] <= v[i]:
                va.append(v[i])
            else:
                va.append(v[i])
                va.append(v[i])
        va = [str(x) for x in va]
        
        print(len(va)) 
        print(' '.join(va))
        