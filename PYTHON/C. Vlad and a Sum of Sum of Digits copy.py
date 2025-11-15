n = int(input())
va = []
print(n//9, n%9)
print()

for i in range(1,n+1):
    v = [int(x) for x in str(i)]
    a = (sum(v))
    va.append(a)
    #print(sum(v))
    
print(sum(va))