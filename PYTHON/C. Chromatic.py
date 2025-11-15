n = int(input())

vve = list(map(int,input().split()))
vaz= list(map(int,input().split()))

vve.sort()
vaz.sort(reverse= True)

#print(vve)
#print(vaz)

vsoma = []

for i in range(n):
    vsoma.append(vve[i]+vaz[i])
#print(vsoma)

dif = max(vsoma) - min(vsoma)
        
print(dif)