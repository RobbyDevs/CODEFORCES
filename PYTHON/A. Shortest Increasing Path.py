def solve():
    x,y = map(int,input().split())
    
    if x < y:
        
        print(2)
    elif x == y or y == 1:
        print(-1)
    else:
        if x -1 <=y:
            print(-1)
        else:
            print(3)
            
    
    
    
for w in range(int(input())):
    
    solve()
    #print("^^^^")