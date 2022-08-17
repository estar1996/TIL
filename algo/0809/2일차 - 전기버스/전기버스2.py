
import sys
sys.stdin = open('sample_input(2).txt')

T = int(input())
for tc in range(1,T+1):
    K, N, M= map(int, input().split(" ")) 
    M_num = list(map(int, input().split(" ")))

    now = 0           # 현위치
    can_go = now+K       # K 만큼 이동한 자리
    charge_station = 0
    count = 0

    while (can_go < N):
        for i in M_num:
            if now < i <= can_go:
                charge_station = i
            elif can_go < i:
                break
            
        if charge_station == -1:
            count = 0
            break
        
        now = charge_station
        can_go = now+K
        count +=1
        charge_station = -1

    print(f'#{tc} {count}')