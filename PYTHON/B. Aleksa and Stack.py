def solve():
    n = int(input())
    
    ans = [3,8,12]
    
    if n == 3:
        print(*ans,sep=' ')
        
    else:
        
        for i in range(n-3):
            val = ans[-1]+1
            while val % (ans[-3]+ans[-2]) == 0:
                val+=1
                
            ans.append(val)
            
        
        print(*ans,sep=' ')
        
    
for w in range(int(input())):
    solve()
    
    