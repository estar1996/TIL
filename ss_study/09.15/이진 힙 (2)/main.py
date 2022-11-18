import sys
sys.stdin = open("input.txt")


def post(n):
    global cnt
    if n <= N:
        post(2 * n)
        arr[n] = cnt
        cnt += 1
        post(2 * n + 1)


T = int(input())
for t in range(1, T + 1):
    cnt = 1
    N = int(input())
    arr = [0] * (N + 1)
    post(1)
    print(f'#{t} {arr[1]} {arr[N // 2]}')