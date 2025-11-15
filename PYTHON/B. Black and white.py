n = int(input())

c = ind = 0
ant = 'N'
s = 0
for i in range(n):
    for j in input():
        if j == ant:
            c+=1
            if c == 2:
                c = 0
                s+=1
            
        else:
            c = 0
    c =0
print(s)
            