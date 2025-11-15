ct = int(input())

for w in range(ct):
    vz = True
    n = int(input())
    
    if (n-1) %3 == 0 or (n+1) %3 == 0:
        print('First')
    else:
        print('Second')