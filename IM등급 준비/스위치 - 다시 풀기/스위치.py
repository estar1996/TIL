import sys
sys.stdin = open("input.txt")


def change_s(A):

    if A == 1:
        return 0
    else :
        return 1


T = int(input())


arr = list(map(int,input().split()))    # 스위치 배열
st = int(input())                       # 학생 수
for i in range(st):
    S,S_num = map(int,input().split())  # S = 성별 S_num = 가지고 있는 자연수


    if S == 1:
        for j in range(8):
            if j+1 >= S_num:
                if (j+1) % S_num == 0:
                    if arr[j] == 1:
                        arr[j] = change_s(arr[j])
                    else :
                        arr[j] = change_s(arr[j])
            else :
                pass
    elif S == 2:
        for k in range(8):
            if k+1 == S_num :
                arr[k] = change_s(arr[k])
                if S_num >= 5:
                    for l in range(8-S_num-1):
                        if arr[k-(l+1)] == arr[k+(l+1)]:
                            if arr[k-(l+1)] == 0:
                                arr[k-(l+1)] = arr[k+(l+1)] = 1
                            else:
                                arr[k-(l+1)] = arr[k+(l+1)] = 0
                            # arr[k-(l+1)] = change_s(arr[k-(l+1)])
                            # arr[k+(l+1)] = change_s(arr[k+(l+1)])
                else:
                    for l in range(S_num-1):
                        if arr[k-(l+1)] == arr[k+(l+1)]:
                            arr[k-(l+1)] = change_s(arr[k-(l+1)])
                            arr[k+(l+1)] = change_s(arr[k+(l+1)])
            
                        

print(*arr)