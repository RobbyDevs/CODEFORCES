for w in range(int(input())):
    n = int(input())
    v = list(map(int,input().split()))
    vp = []
    for i in v:
        if i%2 == 0:
            vp.append(2)
        else:
            vp.append(1)
            
    ans = 0
    while True:
        #print(vp)
        
        for i in range(len(vp)-1):
            if vp[i] == vp[i+1]:
                vp.pop(i)
                ans+=1
                break
            
        else:
            break
    print(ans)
    