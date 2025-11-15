n = int(input())

v = sorted(list(map(int,input().split())))
cv = sum(v)//2
c = 0
moed = 0
i = n

while c <= cv:
    c+=v[i-1]
    moed +=1
    i-=1
print(moed)