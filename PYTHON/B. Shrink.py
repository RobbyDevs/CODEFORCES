for w in range(int(input())):
    
    n = int(input())
    
    v = [1]

    for i in range(n,1,-1):
        v.append(i)
        

    #print(n-2)
    print(*v,sep=' ')