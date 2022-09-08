import sys
sys.stdin = open("input.txt")

MIN , MAX = map(int,input().split())



cnt = 0
for i in range(MIN,MAX+1):
    # print("I:{}".format(i))
    for j in range(2,MAX+1):
        if i % (j**2) == 0:
            cnt += 1



print(MAX - cnt)