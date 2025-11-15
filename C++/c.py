for w in range(int(input())):
    n = int(input())
    
    v = list(map(int,input().split()))
    
    cp = ci = 0
    
    for i in v:
        if i %2 ==0:
            cp+=1
        else:
            ci+=1
    #print(">>>>",end=' ')
    if cp ==0 or ci == 0:
        print(*v, sep=' ')
    else:
        v.sort()
        print(*v,sep=' ')