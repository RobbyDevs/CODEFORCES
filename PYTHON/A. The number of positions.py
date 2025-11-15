n,a,b = map(int,input().split())
c=0
for i in range(a,n):
    for j in range(b,-1,-1):
        
        if i + j +1 == n:
            c+=1

print(c)