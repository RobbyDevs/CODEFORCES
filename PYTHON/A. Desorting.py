for w in range(int(input())):
    
    
    n = int(input())
    
    v = list(map(int,input().split()))
    dis = 1000000000000
    for i in range(n-1):
        if v[i+1] < v[i]:
            print(0)
            break
        
        if v[i+1]-v[i] < dis:
            dis = v[i+1] - v[i]
    
    else:
        if dis == 0:
            print(1)
        else:
            dif = (dis//2)+1
            #print('dis>>',dis)
            
            #print('>>')
            print(dif)