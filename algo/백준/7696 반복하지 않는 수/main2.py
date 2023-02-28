import sys



while 1:
    n = int(sys.stdin.readline())
    res = []
    if n == 0:
        break
    elif n <=10:
        print(n)
    else:
        i = 0
        while 1:
            i += 1
            st = str(i)
            if (len(res)) == n:
                break
            elif i < 100 and i % 11 != 0:
                res.append(i)
                pass
            elif i < 100 and i % 11 == 0:
                pass
            else:
                for x in range(len(st)):
                    tmp = 0
                    for y in range(1,len(st)-x):
                        if st[x] == st[x+y]:
                            tmp += 1
                            i += 10**((len(st) -(y+1)))
                            break
                    if tmp > 0:
                        break
                res.append(i)

        #     for x in range(len(st)):            # i 번째 숫자를 탐색
        #         tmp = 1
        #         for y in range(1,len(st)-x):
        #             if st[x] == st[x+y]:
        #                 i += 10**(len(st) - (x+y) -1)
        #                 tmp += 1
        #                 break
        #
        #             else:
        #                 res.append(i)
        #                 i += 1
        #         if tmp ==2:
        #             break
        #
        # print(len(res))
        #
