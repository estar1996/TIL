import sys
sys.stdin = open('1.txt')

T = int(input())
for tc in range(1,T+1):
    M = int(input())
    lst = list(map(str,input()))
    arr = [0]*10

    for i in range(M):
        arr[int(lst[i])] +=1
    res = 0

    for a in range(len(arr)):
        if res<=arr[a]:
            res=arr[a]
            idx=a
        

    print(f'#{tc} {idx} {res}')
   