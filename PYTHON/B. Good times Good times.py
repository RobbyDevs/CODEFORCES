with open("in.txt","w") as a:
    for i in range(2,1000000001):
        if len(set([x for x in str(i)])) <= 2:
            a.write(f"{str(i)},")

