c= 0
for w in range(int(input())):
    a,b = map(int,input().split())
    
    if a <= b-2:
        c+=1
print(c)