for w in range(int(input())):
    va = []
    k = int(input())
    i = 0
    while len(va) < k:
        i+=1
        if i%3 != 0 and str(i)[len(str(i))-1] != '3':
            va.append(i)
            
    print(va[k-1])