v = []
for w in range(10000):
    
    for s in str(w):
        if s not in '47':
            break
    else:
        v.append(w)
        

for w in range(len(v)-1):
    print(v[w+1] - v[w])
