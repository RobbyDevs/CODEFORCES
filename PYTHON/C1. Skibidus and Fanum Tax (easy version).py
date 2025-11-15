for w in range(int(input())):
    
    n,m = map(int,input().split())
    
    v = list(map(int,input().split()))
    b = int(input())
    
    if n ==1:
        print('YES')
      
    else:
        
        v[0] = min(b-v[0],v[0])
        
        for i in range(1,n):
            if min(v[i],b-v[i]) >= v[i-1]:
                v[i] = min(v[i],b-v[i])
            else:
                v[i] = max(b-v[i],v[i])
                
        for i in range(n-1):
            if v[i] > v[i+1]:
                print('NO')
                break
        else:
            print('YES')    