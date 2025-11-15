import math
def possible(a):
    if math.sqrt(a) % 1 == 0:
        return str(int(math.sqrt(a))) + ' 0' 
    return -1

t = int(input())
for i in range(t):
    a = int(input())
    print(possible(a))