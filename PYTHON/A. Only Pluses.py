for w in range(int(input())):
    
    v = list(map(int,input().split()))
    
    for i in range(5):
        v.sort()
        v[0]+=1
        
    print(v[0]*v[1]*v[2])