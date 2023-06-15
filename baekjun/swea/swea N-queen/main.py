import sys
sys.stdin = open('input.txt')


T = int(input())


def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            return False
    return True

def n_queens(x):
    global ans
    if x == N:
        ans += 1
        return
    else:
        for i in range(N):
            row[x] = i
            if is_promising(x):
                n_queens(x+1)



for tc in range(1,T+1):
    N = int(input())
    ans = 0
    row = [0] * N

    n_queens(0)
    print(ans)
