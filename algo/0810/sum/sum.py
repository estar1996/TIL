import sys


import sys
sys.stdin = open('sum_input.txt')

T = 10
for tc in range(1,T+1):
    t = int(input())
    N = 100
    arr = [list(map(int,input().split())) for _ in range(N)]

    max_i = 0
    for i in range(N):
        sum = 0
        for j in range(N):
            sum += arr[i][j]
        if sum > max_i:
            max_i = sum

    max_j = 0
    for i in range(N):
        sum = 0
        for j in range(N):
            sum += arr[j][i]
        if sum > max_j:
            max_j = sum

    max_d = 0
    for i in range(N):
        sum_l = 0
        sum_r = 0
        sum_l += arr[i][i]
        sum_r += arr[i][99-i]
    if max(sum_l,sum_r) > max_d :
        max_d = max(sum_l,sum_r)

    max_ijd = [max_i,max_j,max_d]
    max_num = max_ijd[0]
    for i in max_ijd:
        if i > max_num:
            max_num = i
            

    print('#{} {}'.format(t,max_num))



# T = 10
# for tc in range(1,11):
#     t = int(input())
#     arr = [list(map(int,input().split()))for _ in range(N)]


