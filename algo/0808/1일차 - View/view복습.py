import sys
sys.stdin = open("input.txt")

T = 10
for tc in range(1,T+1):
    M = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    for i in range(2,M-2):
        
        if arr[i] > arr[i-2] and arr[i] > arr[i-1] and arr[i] > arr[i+1] and arr[i] > arr[i+2] :
            a = arr[i]-arr[i-2]
            b = arr[i]-arr[i-1]
            c = arr[i]-arr[i+1]
            d = arr[i]-arr[i+2]
            min_abcd = a
            
            for j in [a,b,c,d]:
                if j < min_abcd:
                    min_abcd = j
            cnt += min_abcd

    print("#{} {}".format(tc,cnt))