l,b = map(int,input().split())
i=0
while l <= b:
    l *= 3
    b *= 2
    i+=1
print(i)