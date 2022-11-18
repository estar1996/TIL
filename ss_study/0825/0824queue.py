T = 10
 
for _ in range(1,T+1):
 
    tc = int(input())
    pw = list(map(int,input().split()))
 
    while pw[-1] > 0:
        for i in range(1,6):
            if pw[0] -i > 0:
                pw.append(pw.pop(0)-i)
            else:
                pw.pop(0)
                pw.append(0)
                break
    print("#{} {} {} {} {} {} {} {} {}".format(tc,*pw))