c = int(input())

n = c//9
m = c%9
s = 0
ss= 0
vs = []
a = 0
#print(n,m)

#an = ((45 + (8*9))*4)//2
an = 45 + (n-2)*9
print(an)


#print(an)#ok

sn = ((45+an) *(n-1))//2

sn+=45

print(sn)

for i in range((n*9)+1,(n*9)+m+1):
    s = [int(x) for x in str(i)]
    a = (sum(s))
    vs.append(a)
    
    
    #print(sum(v))
#print(sum(vs))
print(sum(vs)+sn)
