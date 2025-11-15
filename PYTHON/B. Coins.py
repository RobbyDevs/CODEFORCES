n = int(input())
v = [n]
va = []
for i in range((n//2+1),1,-1):
    if n%i == 0:
        v.append(i)