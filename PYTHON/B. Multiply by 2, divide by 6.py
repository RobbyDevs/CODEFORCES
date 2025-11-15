dic = {6:1,3:2,18:3,108:4,648:5,3888:6,23328:7,139968:8,839808:9,5038848:10,30233088:11,181398528:12,1088391168:13}

def solve():
    n = int(input())
    
    if n == 1:
        print('0')
        return
    
    else:
        ans = 0
        flag = 0
        #print('vvvvv')
        while True:
            flag+=1
            if flag > 100:
                print(-1)
                return
            
            if n in dic:
                ans+=dic[n]
                print(ans)
                return
            if n %6 == 0:
                n = n//6
                ans+=1
            else:
                n=n*2
                ans+=1
                

    
for w in range(int(input())):
    solve()
    
    
"""

3 | 6 | 18 | 

2 > 4 > 8 > 16 > 

12 > 24 > 48

18
108
648
3888
23328
139968
839808
5038848
30233088
181398528
1088391168

"""