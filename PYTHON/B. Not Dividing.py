for w in range(int(input())):
    n = int(input())
    
    v = list(map(int,input().split()))
    
    for i in range(n-1):
        if v[i] == 1:
            v[i]+=2
        if (v[i+1]-v[i] > 1):
            v[i]+=(abs(v[i+1]-v[i]-1))
        elif (v[i+1]-v[i] < -1):
            v[i+1]+=(abs(v[i+1]-v[i]))
            
    print(*v,sep=" ")