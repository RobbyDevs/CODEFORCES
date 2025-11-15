v = [str(x) for x in input()]
va = []
s = 'hello'
c = 0

k = 0
for i in range(len(s)):
    for j in range(k,len(v)):
        if s[i] == v[j]:
            va.append(v[j])
            k = j+1
            break

if ''.join(va) == 'hello':
    print('YES')
else:
    print('NO')