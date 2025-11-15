import sys

input = sys.stdin.readline


def solve():
    a,b,soma,xor = map(int,input().split())
    c1 = c2 = 0
    ans = 0
    if a == b:
        print(0)
    elif a > b:
        if a%2 == 1 and a-b == 1: # impar
            print(xor)
        else:
            print(-1)
    else:
        for i in range(a,b):
            if i %2 == 0:
                ans+= min(soma,xor)
            
            else: 
                ans+=soma
        print(ans)

for w in range(int(input())):
    solve()
    
"""
se i eh impar, i somaor 1 = i-1
se i erh par  i somapr 1 = i+1

i+1 = soma
i^1 = xor

"""