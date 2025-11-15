va = list(map(int,input().split()))

v = list(map(int,input().split()))

for i in range(len(v)-1):
    if v[i+1]%v[i] != va[i]:
        print(f'Nop: {v[i+1]} % {v[i]} == {v[i+1]%v[i]}')    
        break
else:
    print('YEP')