import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    p1 = []
    p2 = []
    for i in range(4):
        if i == 0 or i == 2 :
            p1.append(arr[i])
        else:
            p2.append(arr[i])
    for _ in range(4):
        arr.pop(0)

    res = 0

    for a in range(4):

        if len(arr) > 0:
            p1.append(arr.pop(0))
            p2.append(arr.pop(0))
        p1 = sorted(p1)
        p2 = sorted(p2)
        for x in range(len(p1)-2):
            if p1[x] == p1[x+1] == p1[x+2]:
                res += 1
                break
            elif p1[x+1]-p1[x] == 1 and p1[x+2]-p1[x+1] == 1:
                res += 1
                break
            elif p2[x] == p2[x+1] == p2[x+2]:
                res += 2
                break
            elif p2[x+1]-p2[x] == 1 and p2[x+2]-p2[x+1] == 1:
                res += 2
                break

    if res == 1:
        print("#{} {}".format(tc,res))
    elif res == 2:
        print("#{} {}".format(tc, res))
    elif res == 0:
        print("#{} {}".format(tc, res))