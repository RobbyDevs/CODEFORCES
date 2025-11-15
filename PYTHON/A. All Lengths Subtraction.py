def solve():
    n = int(input())
    
    v = list(map(int,input().split()))
    
    mai = max(v)
    flag = n
    
    
    
    while sum(v) >0:
        #print(v,"|",flag)
        
        mai = max(v)
        prox = 0
        
        
        if len(v) <=2 :
            flag -= mai
            #print(mai)
            break
        
        for i in range(len(v)):
            if v[i] == mai:
                if i ==0:
                    prox = v[i+1]
                elif i == len(v)-1:
                    prox = v[len(v)-2]
                    
                else:
                    prox = max(v[i+1],v[i-1])
                    
                flag -= abs(mai-prox)
                del v[i]
                break
                    
    if flag >=0:
        print("YES")
    else:
        print("NO")
    
    
    
for w in range(int(input())):
    
    solve()
    
    
"""
5
1 5 3 4 2

2
"""    
