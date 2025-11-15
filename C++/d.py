import sys
from math import gcd
sys.stdin.readline
#crivo
n = 100000
primo = [1] * (n + 1)
primo[0] = primo[1] = 0

p = 2
while p * p <= n:
    if primo[p]:
        for i in range(p*p, n+1, p):
            primo[i] = 0
    p += 1


ans = 1
i = 2
cont = 0
while len(str(ans))<19:
    if primo[i]:
        print(i)
        ans = ans*i
        print(ans)
        cont+=1
    i+=1
    
print(cont,i)
        
