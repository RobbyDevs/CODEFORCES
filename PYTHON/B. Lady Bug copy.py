for _ in range(int(input())):
    n=int(input())
    l=input()
    m=input()
    if ((l[::2].count("1"))<=(m[1::2].count("0"))) and ((l[1::2].count("1"))<=(m[0::2].count("0"))):
        print("YES")
    else:
        print("NO")