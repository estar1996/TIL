import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = []
    o_map = [[0]*7 for _ in range(7)]
    o_map[3][3],o_map[4][4] = 2,2
    o_map[4][3],o_map[3][4] = 1,1


    # print(o_map)
    for _ in range(M):
        lst = list(map(int,input().split()))
        arr.append(lst)

    for i in range(M):
        if arr[i][2] == 1:
            if o_map[arr[i][0]][arr[i][1]] == 0:
                o_map[arr[i][0]][arr[i][1]] = 1
            elif o_map[arr[i][0]][arr[i][1]] == 2:
                if o_map[arr[i+1][0]][arr[i+1][1]] == 1 or o_map[arr[i-1][0]][arr[i-1][1]] == 1 or o_map[arr[i+1][0]][arr[i][1]] == 1 or o_map[arr[i][0]][arr[i+1][1]] == 1 or o_map[arr[i-1][0]][arr[i][1]] == 1 or o_map[arr[i][0]][arr[i-1][1]] == 1:
                    # 위 아래 좌 우 대각선이 1이라면 ~
                    o_map[arr[i][0]][arr[i][1]] = 1
        elif arr[i][2] == 2:
            if o_map[arr[i][0]][arr[i][1]] == 0:
                o_map[arr[i][0]][arr[i][1]] = 2
            elif o_map[arr[i][0]][arr[i][1]] == 1:
                if o_map[arr[i+1][0]][arr[i+1][1]] == 2 or o_map[arr[i-1][0]][arr[i-1][1]] == 2 or o_map[arr[i+1][0]][arr[i-1][1]] or o_map[arr[i-1][0]][arr[i+1][1]] or o_map[arr[i+1][0]][arr[i][1]] == 2 or o_map[arr[i][0]][arr[i+1][1]] == 2 or o_map[arr[i-1][0]][arr[i][1]] == 2 or o_map[arr[i][0]][arr[i-1][1]] == 2:
                    # 위 아래 좌 우 대각선이 2이라면 ~
                    o_map[arr[i][0]][arr[i][1]] = 2

    w_cnt = 0
    b_cnt = 0
    for j in range(7):
        for k in range(7):
            if o_map[j][k] == 2:
                w_cnt += 1
            elif o_map[j][k] == 1:
                b_cnt += 1
    print(w_cnt,b_cnt)