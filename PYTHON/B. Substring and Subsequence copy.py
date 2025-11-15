import sys

input = sys.stdin.readline


def solve():
    a = input().strip()
    b = input().strip()

    
    ans = len(a)+len(b)
    vans = []
    dif = 0
    ind = 0
    
    
    for i in range(len(b)):
        for j in range(ind,len(a)):
            if b[i] == a[j]:
                ind = j+1
                dif +=1
                break
        
    
    print(ans-dif)
    
for w in range(int(input())):
    solve()
    
"""
a = substring
b = subsequencia

cde
abcefg

cde

ans >= len(a)
"""