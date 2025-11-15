n = int(input())

im = 'I hate'
pa = 'I love'
con = 'that'
fim = 'it'
v = []
for i in range(1,n+1):
    
    if i %2 != 0:
        v.append(im)
  

    if i %2 == 0:
        v.append(pa)
        
print(' that '.join(v), end=' ')
print(fim)
