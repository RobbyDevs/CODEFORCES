def solve():
    a,b = map(int,input().split())
    
    ba = bin(a)[2:]
    bb = bin(b)[2:]
    
    
    if (len(ba)<len(bb)):
        print(-1)
        return
    
    if (a==b):
        print(0)
    
    else:
        ans1 = ''
        for i in ba:
            if i =='0':
                ans1+='1'
            else:
                ans1+='0'
            
                
        #print(ba)
        aa = '1'*len(ba)
        #print(ans1)
        
        #print(bb)

        ans2 = int(aa,2)^b
        print(2)
        print(int(ans1,2),ans2)
    
    
for i in range(int(input())):
    
    solve()
