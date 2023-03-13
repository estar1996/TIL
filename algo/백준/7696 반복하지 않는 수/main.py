
# sys.stdin = open('input.txt')
import sys



while 1:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    res = 0
    i = 0
    while res != n:
        i += 1
        st = str(i)
        s = set(str(i))

        if len(s) == len(str(i)):
            res += 1
            if res == n:
                print(i)
                break

    # print(res)
        # else:
        #
        #     for x in range(len(st)):
        #         tmp = 0
        #         for y in range(x+1,len(st)):
        #             if st[x] == st[y]:
        #                 i += 10**(len(st)-y -1)
        #                 i -= 1
        #                 tmp +=1
        #                 break
        #         if tmp != 0:
        #             break



    #
    # lst = [i for i in range(1,n+1)]
    # res = []
    # while len(res) == n:


    # print(i)
