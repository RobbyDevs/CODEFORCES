n = int(input())
h = ve = 0
v = []
va = []
for i in range(n):
    h += sum(list(map(int,input().split())))
    
if h == 0:
    print('YES')
else: print('NO')