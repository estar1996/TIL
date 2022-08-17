import sys
sys.stdin = open("input(1).txt")


def check(a):
    max_a = 0
    for i in range(N):
        for j in range(N):
            for k in range(0,N+1):
                if a[i][j:k] == a[i][j:k][::-1] and (k-j) > max_a:
                    max_a = k-j
    return max_a

T = 10

for x in range(1, T+1):
    tc = int(input())
    N = 100
    arr = [list(input()) for _ in range(100)]
    arr2 = list(zip(*arr))
    res = 0
    if check(arr) > check(arr2):
        res = check(arr)
    else:
        res = check(arr2)

    print("#{} {}".format(tc,res))