from math import ceil
from math import floor


for w in range(int(input())):
    n = int(input())
    
    w = n
    l = 0
    ans = 0
    
    while True:
        if w>1:
            ans += w//2
            l +=w//2
            w = w - (w//2)
            
        
        if l>1:
            ans+=l//2
            l = l - (l//2)
        
        if l+w <=2:
            ans+=1
            break
        
        

        
    print(ans)
        
        
        
        