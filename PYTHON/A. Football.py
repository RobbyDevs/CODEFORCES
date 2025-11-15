v = input()
c  = 9
d = 1

for i in v:
    if d >= 7:
        print('YES')
        break
    
    if c == i:
        d+=1
    else:
        d = 1
    c = i

else:
    if d>=7:
        print("YES")
    else:
        print('NO')