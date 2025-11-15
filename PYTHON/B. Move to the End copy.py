for w in range(int(input())):
    
    n = int(input())
    
    v = list(map(int,input().split()))
    vs = [v[-1]]
    ind = 0
    
    for i in range(len(v)-1,0,-1):
        vs.append(v[i-1]+vs[ind])
        ind+=1
        
    vs.append(0)
    j = len(vs)-1
    for i in range(n):
        va = list(v)
        mai = max(va[:n-i])
        
        #print(mai)
        
        va.pop(v.index(mai))
        va.append(mai)

        #print(va)
        #print()
        #print(mai)
        #print('soma',vs[i])
        print(mai+vs[j-i],end=' ')
    print()
        #j-=1
    
