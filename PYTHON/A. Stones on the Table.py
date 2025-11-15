n = int(input())

v = [str(x) for x in input()]

c = 0
for i in range(len(v)-1):
    if v[i+1] == v[i]:
        c+=1
    

print(c)