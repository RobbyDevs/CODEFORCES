n = int(input())

v = [str(x) for x in input() if x != ' ']
vs = ''.join(v)
vi = []
for i in range(1,n-1):
    if v[i] == '0' and v[i+1] == v[i-1] and v[i+1] == '1':
        vi.append(i)
        
if len(v)==0:
    print(0)
    
else:
    c = 0
    for i in range(len(vi)):
        v[vi[i]] = '0'


    for i in range(1,n-1):
        if v[i] == '0' and v[i+1] == v[i-1] and v[i+1] == '1':
            c+=1
        
    print(c)

    print(vi)
    print(''.join(v))
# 10
# 1010101010

#1 1 0 0 1 0 0 0 1 0

