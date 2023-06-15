
N , M = map(int,input().split())

arr = []
res = []
for _ in range(N):
    arr.append(input())

for i in range(N-7):
    for j in range(M-7):
        # arr[i][j]
        cnt1 = 0
        cnt2 = 0
        for r in range(i,i+8):
            for c in range(j,j+8):
                if (r+c) % 2 == 0:
                    if arr[r][c] != 'W':
                        cnt1 += 1
                    if arr[r][c] != 'B':
                        cnt2 += 1
                else:
                    if arr[r][c] != 'B':
                        cnt1 += 1
                    if arr[r][c] != 'W':
                        cnt2 += 1
        res.append(min(cnt1,cnt2))


print(min(res))
