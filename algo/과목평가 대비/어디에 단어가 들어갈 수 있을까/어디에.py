
import sys
sys.stdin = open("input (1).txt")

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    res = 0
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            elif arr[i][j] == 0:
                if cnt == K:
                    res += 1
                cnt = 0
        else:                            
            if cnt == K:                            
                res += 1                                        
            cnt = 0     
                
    for j in range(N):
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
            elif arr[i][j] == 0:
                if cnt == K:
                    res += 1
                cnt = 0
        else:                                                   
            if cnt == K:                                            
                res += 1                                         
            cnt = 0     

    print("#{} {}".format(tc,res))