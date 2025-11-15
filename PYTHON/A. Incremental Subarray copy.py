def solve():
    n,m = map(int,input().split())
    vm = list(map(int,input().split()))
    
    v = []
    p = 1
    ans = 1
    
    if [1,1] in vm:
        print(ans)
        return
    
    while p <=n:
        for i in range(1,p):
            v.append(i)
        p+=1
        
    print(v)
    print(vm)
    indv  = 0
    indvm = 0
    count = 0
    
    for i in range(len(v)):            
        if count == len(vm):
            ans+=1
            count = 0
        
        for j in range(indvm,len(vm)):
            if vm[j] == v[i]:
                indvm = j+1
                count +=1
                break
            
    print(ans)
                            
    
for w in range(int(input())):
    solve()