s = 'codeforces'
for w in range(int(input())):
    v = input()
    c =0
    for i in range(len(v)):
        if v[i]!= s[i]:
            c+=1
        
    print(c)