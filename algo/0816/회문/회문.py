import sys
sys.stdin = open("sample_input(1).txt")

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(str,input()))for _ in range(N)]

    
    res =[]
    for i in range(N):
        for j in range(N-M+1):
            
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]:
                res.append("".join(arr[i][j:j+M]))
            

    for j in range(N):
        for i in range(N-M+1):
            col_lst = []
            for k in range(M):
                col_lst.append(arr[i+k][j])
            if col_lst == col_lst[::-1]:
                res.append("".join(col_lst))


    print("#{} {}".format(tc,*res))