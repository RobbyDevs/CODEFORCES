e = []
d = []


for w in range(int(input())):
    lado,cor = input().split()
    if lado == 'E':
        e.append(cor)
        
    else:
        d.append(cor)
print(e)
print(d)