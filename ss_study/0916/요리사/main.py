T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    # print(arr)
    b_lst = [[0]*(N+1) for _ in range(N+1)]

    for i in range(1,N+1):
        for j in range(1,N+1):
            if i != j:
                b_lst[i][j] += arr[i-1][j-1]
                b_lst[i][j] += arr[j-1][i-1]
                arr[i - 1][j - 1] = 0
                arr[j - 1][i - 1] = 0
    # print(b_lst)
    res_lst = []
    for k in range(N+1):
        for l in range(N+1):
            if b_lst[k][l] != 0:
                res_lst.append(b_lst[k][l])
    print(res_lst)


# 1
# 4
# 0 5 3 8
# 4 0 4 1
# 2 5 0 3
# 7 2 3 0