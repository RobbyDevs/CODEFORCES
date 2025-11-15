n = int(input())
c = 0
while n/5 > 5:
    n = n /5
    c+=n
    print(n,c)
    
    
if n > 1:
    print(int(c)+1)
else:
    print(int(c))