import sys
sys.stdin = open("sample_input(1).txt")

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    arr = [list(map(int,input())) for _ in range(N)]
    print(arr)
    x1 = 0                                  # 출발지
    y1 = 0

    x2 = 0                                  # 도착지
    y2 = 0

    dr = [1,-1,0,0]
    dc = [0,0,-1,1]


    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                x1 = i
                y1 = j
            elif arr[i][j] == 3:
                x2 = i
                y2 = j

    for r in range(N):
        for c in range(N):





    print(x,y)