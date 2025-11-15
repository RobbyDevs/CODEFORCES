n = int(input())

v = [str(x) for x in input() if x != ' ']
vs = ''.join(v)
vi = []
c = 0
for i in range(1,n-1):
    if v[i] == '0' and v[i+1] == v[i-1] and v[i+1] == '1':
        v[i+1] = '0'
        c+=1
        
print(c)

