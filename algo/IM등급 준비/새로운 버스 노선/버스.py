import sys
sys.stdin = open("sample_in.txt")

T =int(input())

for tc in range(1,T+1):
    N = int(input())
    bus = []
    for _ in range(1,N+1):
        b = list(map(int,input().split()))
        bus.append(b)
    
    lst = [0]*len(bus)                              # 가장 긴 노선을 구하기 위한 .. 0으로 구성된 리스트
    for q in range(len(bus)):
        lst[q] += bus[q][-1]

    cnt = [0]*max(lst)                             # 임시로 20개만
    for i in range(len(bus)):
        a = bus[i][1]
        b = bus[i][-1]
        if bus[i][0] == 1:                     # 일반 버스 A번부터 B번 사이의 모든 정류장에 정차
            for j in range(a,b+1):
                cnt[j] += 1
        elif bus[i][0] == 2:                    # 급행 버스는 출발 정류장 번호가 짝수라면 짝수마다 정차, 홀수라면 홀수마다 정차.
            if bus[i][1] % 2 == 0:
                for k in range(a,b+1):
                    if k % 2 == 0:
                        cnt[k] += 1
            
            else :
                for k in range(a,b+1):
                    if k % 2 == 1:
                        cnt[k] += 1
        else :                                  # 광역 급행 버스는 A가 짝수인 경우 A 와 B 사이의 모든 4의 배수 번호 정류장에, A 가 홀수인 경우 A와 B 사이의 3의 배수이면서 10의 배수가 아닌 번호 정류장에 정차한다.
            if bus[i][1] % 2 == 0:
                for l in range(a,b+1):
                    if k % 4 == 0:
                        cnt[l] += 1
            else :
                for l in range(a,b+1):
                    if k % 3 == 0 and k % 10 != 0:
                        cnt[l] += 1 
    res = 0
    for a in range(len(cnt)):
        if cnt[a] > 1:
            res += 1
    print("#{} {}".format(tc,res))