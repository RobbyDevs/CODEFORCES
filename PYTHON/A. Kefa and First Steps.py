n = int(input())

v = list(map(int,input().split()))
c = 1
s = 1

for i in range(n-1):
    if v[i+1]>= v[i]:
        c +=1
    else:
        if c > s:
            s = c
            
        c = 1
        
print(max(c,s))