v = [] 
c = 1
for w in range(int(input())):
    v.append(input())
    
for i in range(1,len(v)):
    if v[i-1][1] == v[i][0]:
        c+=1
        
print(c)