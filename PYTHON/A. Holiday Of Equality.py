n = int(input())

v = list(map(int,input().split()))

ma = max(v)
c = 0
for i in v:
    c+= ma-i
    
print(c)