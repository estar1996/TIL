A, B = map(int,input().split())
tmp = B

res = 0
while tmp != A:

    if tmp % 10 == 1:
        tmp //= 10
        res += 1
    elif tmp % 2 == 0:
        tmp /= 2
        res += 1
        print(tmp)
    else:
        print(-1)

print(res)