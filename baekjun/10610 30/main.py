N = input()

if "0" not in N:
    print(-1)
else:
    num = 0
    for i in range(len(N)):
        num += int(N[i])
    if num % 3 == 0:
        sorted_num = sorted(N,reverse=True)
        for i in sorted_num:
            print(i,end="")
    else:
        print(-1)