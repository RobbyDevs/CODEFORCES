a,b = map(int,input().split())
c = 0
for i in range(b):
    if a % 10 ==0:
        a = a//10
        c +=1
    else:
        a -=1
        c+=1
print(a)