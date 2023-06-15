import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1,T+1):

    N = int(input())

    n1 = N//2
    n2 = N//2

    temp1 = 0
    for k in range(2, n1):
        if n1 == 0 and n2 == 0:
            print(1,0)
            break
        elif n1 % k == 0 or n2 % k == 0:
            temp1 += 1
            break
        elif n1 == 0 and n2 == 0:
            print(n1,n2)
    if temp1 == 0:
        print(n1, n2)

    else:
        n1 += 1
        n2 += 1
        for _ in range(N//4):
            n1 += 2
            n2 -= 2
            temp = 0
            for i in range(2,n1):
                if n1 % i == 0 or n2 % k == 0:
                    temp += 1
                    break
            if temp == 0:
                print(n1,n2)
                break




    # if N % 2 == 0:
    #     n2 = n1
    #
    # if n1 % 2 != 0:
    #     temp1 = 0
    #     for k in range(2,n1):
    #         if n1 % k == 0 or n2 % k ==0:
    #             temp1 += 1
    #             break
    #     if temp1 == 0:
    #         print(n1,n2)
    #     else:
    #         for _ in range(0, N // 2 + 1):
    #             n1 -= 1
    #             n2 += 1
    #             if n1 % 2 != 0:
    #                 temp2 = 0
    #                 for a in range(2, n1):
    #                     if n1 % a == 0 or n2 % a == 0:
    #                         temp2 += 1
    #                         break
    #                 if temp2 == 0:
    #                     print(n1, n2)
    #                     break
    # else:
    #     for i in range(0,N//2+1):
    #         n1 -= 1
    #         n2 += 1
    #         if n1 % 2 != 0 :
    #             temp2 = 0
    #             for j in range(2,n1):
    #                 if n1 % j == 0 or n2 % j ==0:
    #                     temp2 += 1
    #                     break
    #             if temp2 == 0:
    #                 print(n1,n2)
    #                 break