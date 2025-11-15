for w in range(int(input())):
    
    n = int(input())
    v = list(map(int,input().split()))
    c2 =0
    va = []
    for i in range(len(v)):
        if v[i] ==2:
            c2+=1
            va.append(i+1)
            
    if c2 == 0:
        print(1)
    elif c2 %2!=0:
        print(-1)
    else:
        ind = (c2//2)-1
        
        print(va[ind])