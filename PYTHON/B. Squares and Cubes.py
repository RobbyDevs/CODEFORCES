import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    
    p = 1
    ans = 0
    
    v = set()
    while p*p <= n:
        if p*p <=n:
            v.add(p*p)
        if p*p*p <=n:
            v.add(p*p*p)
            
        p+=1
    print(len(v))  
    
for w in range(int(input())):
    solve()