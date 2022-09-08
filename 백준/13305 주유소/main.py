import sys
sys.stdin = open('input.txt')

N = int(input())
L = list(map(int,input().split()))
P = list(map(int,input().split()))


cnt = 0
temp = P[0]
for i in range(0,N-1):
    if P[i] <= temp:
        cnt += P[i] * L[i]
        temp = P[i]
    elif i == N-1:
        break
    else:
        cnt += temp * L[i]
print(cnt)