for w in range(int(input())):
    n = int(input())
    v = [int(x) for x in input()]
    
    #print(v)
    
    c1 = v.count(1)
    c0 = v.count(0)
    
    if min(c1,c0) == 0:
        print(0)
        print()
        
    else:
        ans = []
        
        for i in range(n):
            if v[i] == 1:
                ans.append(i+1)
        
        print(len(ans))
        print(*ans,sep=' ')
        