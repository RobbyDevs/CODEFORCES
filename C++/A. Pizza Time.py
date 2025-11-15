from math import ceil
for w in range(int(input())):
    
    n = int(input())
    ans = 0
    div = n
    mod = 0
    
    
    while div>2:
        ans +=div//3
        mod = div%3
        div = div//3
        
        if mod == 2:
            div+=2
        if mod == 1:
            div+=1
            
    print(ans)
    