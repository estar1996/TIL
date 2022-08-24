from cgitb import reset
import sys
sys.stdin = open("input (1).txt")

T = int(input())
for tc in range(1,T+1):
    N , M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    temp = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            res = 0
            for a in range(M):    
                for b in range(M):
                    res += arr[i+a][j+b]
                    temp.append(res)
        result = 0
        for c in temp:
            if c > result:
                result = c

    print("#{} {}".format(tc,result))

    #2 159
#3 428
#4 620
#5 479
#6 941
#7 171
#8 968
#9 209
#10 1242

