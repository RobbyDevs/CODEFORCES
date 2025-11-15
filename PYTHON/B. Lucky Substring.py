v = int(input())

v = [x for x in str(v)]
f = s = 0
for i in v:
    if i == '4':
        f +=1
    elif i == '7':
        s +=1
        
if s + f != 0:
        
    if s>f:
        print(7)
    else:
        print(4)
else:
    print(-1)