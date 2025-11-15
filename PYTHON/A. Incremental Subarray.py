def solve():
    n,m = map(int,input().split())
    vm = list(map(int,input().split()))
    
    v = []
    p = 1
    ans = 1
    
    

    mai = max(vm)
    for i in range(m-1):
        if vm[i] >= 1 and vm[i+1] == 1:
            print(ans)
            return
    
    
    ans += n-max(vm)
    
    print(ans)

    

    #print(ans)
                            
    
for w in range(int(input())):
    solve()