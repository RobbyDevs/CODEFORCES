n,t = map(int,input().split())
s = 0
for i in range(n):
    a,b = input().split()
    s +=int(b)
    
print(f'{(s/t):.5f}')