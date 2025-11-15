n = [int(x) for x in input() if x == '4' or x == '7']


cs = str(len(n))
s ='47'
c = True
for i in cs:
    if i not in s:
        print("NO")
        c = False
        break

if c == True:
    print("YES")