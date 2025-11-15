n = int(input())

s = input()

c = 0
r = 0

for i in s:
    if i == 'x':
        c+=1
        
        if c>2:
            r+=1
    else:
        c=0
print(r)