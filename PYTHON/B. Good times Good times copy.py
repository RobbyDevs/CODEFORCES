v = []
for i in range(2,int(input())):
    if len(set([x for x in str(i)])) <= 2:
       v.append(i)
       

for i in range(1,len(v)):
    print(v[i]-v[i-1],end=' ')
    
for w in range(int(input())):
    n = int(input())

    c = 0
    for i in range(2,200000001):
        if c>20:break
        if len(set([x for x in str(i)])) <= 2:
            if len(set([y for y in str(i*n)])) <= 2:
                c+=1
                print(i)
    else:
        print(2)
        
        
"""

1 2 1 9 2 8 3 7 4 6 5 5 6 4 7 3 8 1 2 9 1 8 
1 3 1 9 2 8 3 7 4 6 5 5 6 4 7 1 3 8 2 9 1 7
1 4 1 9 2 8 3 7 4 6 5 5 6 1 4 7 3 8 2 9 1 6


121 1
122 1
    10
131 2
133 2
    10
141

"""