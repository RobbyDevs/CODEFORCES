n = int(input())

v = list(map(int,input().split()))

va = [int(0) for x in range(n)]

#print(va)
for i in range(n):
    va[v[i]-1] = str(i+1)
    
print(' '.join(va))