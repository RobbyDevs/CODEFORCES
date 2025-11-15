for w in range(int(input())):
    l = int(input())
    
    va = input()
    vb = input()
    r = 0
    c = 0
    for i in range(l):
        if va[i] == "1":
            r = 1
            if i>0:
                if vb[i-1]=="0":
                    c+=1
                else:
                    c-=1
            if i<l-1:
                if vb[i+1] == "0":
                    c+=1
                else:
                    c-=1
    if r ==0:
        print("YES")
        
    elif c <0:
        print('NO')
    else:
        print('YES')