for i in range(int(input())):
    n = int(input())
    v = input()
    va = [v[0]]
    
    for i in range(n):
        if (va[-1]!=v[i]):
            va.append(v[i])
            
    #print(va)
    vb = ["01","10"]
   # print(">>>",end='')
    if(''.join(va) in vb):
        print(2)
    else:
        print(1)





"""
101

1010


0 - 101 010 00
1 = 101 010 11
10 = 100
01 = 001

101


"""
