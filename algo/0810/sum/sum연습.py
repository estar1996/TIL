import sys
sys.stdin = open('sum_input.txt')

T = 10

for __ in range(1,T+1):
    N = 100
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    res_lst = []
    for i in range(N):
        sum_r = 0
        for j in range(N):
            sum_r += arr[i][j]
        res_lst.append(sum_r)

    res_lst2 = []
    for j in range(N):
        sum_c = 0
        for i in range(N):
            sum_c += arr[i][j]
        res_lst2.append(sum_c)
    
    res_lst3 = []
    for a in range(N):
        sum_d = 0
        sum_d += arr[a][a]
        res_lst3.append(sum_d)

    res_final = res_lst + res_lst2 + res_lst3
    max_res = 0
    for i in range(len(res_final)):
        if max_res < res_final[i]:
            max_res = res_final[i]
    
    print(max_res)