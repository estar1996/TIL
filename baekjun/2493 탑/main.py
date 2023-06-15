import sys
sys.stdin = open("input.txt")

N = int(input())
lst = list(map(int,input().split()))
res = [0]*N
for i in range(0,N):
    for j in range(1,N - i):
        if lst[N-1-i-j] > lst[N-1-i]:
            res[N-1-i] += N-i-j
            break
print(*res)
#         print(lst[N-1-i-j])