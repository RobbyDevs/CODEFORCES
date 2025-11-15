t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    l = [int(i) for i in input().split()]
    l.sort(reverse=True)
    t=[]
    for i in range(len(l)):
        if i==0:
            t.append(l[i])
            s=0
        elif sum(l)<k:
            s+= k-sum(l)
            break
        if sum(t)==k:
            break
        else:
            if i==n-1:
                if sum(t)==k:
                    break
                else:
                    t.append(l[i])
                    if sum(t)==k:
                        break
                    else:
                        s+= (k - sum(t))
                        break
            else:
                if sum(t)==k:
                    break
                elif sum(t)<k and (sum(t)+l[i+1])>k:
                    s+= (k - sum(t))
                    break
                else:
                    t.append(l[i+1])
    print(s)