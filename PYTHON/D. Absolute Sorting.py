for w in range(int(input())):
    n = int(input())
    
    v = list(map(int,input().split()))
    
    ans = int(input())
    
    if ans == -1:
        continue
    for i in range(n):
        v[i] = abs(v[i]-ans)
        
    
    print(v)
    
    
"""
10 5 4 3 2 1


se estiver ordenado, ans = 0
se estiver revertido, ans = max(v)+1



"""
