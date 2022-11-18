import sys
import math
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1,T+1):
    N = int(input())


    for i in range(1,int(N**(1/3)+2)):
        if N == i**3 :
            print("#{} {}".format(tc,i))
            break
    else:
        print("#{} {}".format(tc, -1))

# t = int(input())
# for tc in range(t):
#     n = int(input())
#     for i in range(1, int(n**(1.0/3.0))+2):
#         if i**3 == n:
#             print(f'#{tc + 1} {i}')
#             break
#     else:
#         print(f'#{tc + 1} -1')