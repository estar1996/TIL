

def solve(cnt):
    # 교환 했을 때 모양
    num = ''.join(cards)
    num = int(num)

    if cnt == N:
        return
    # 교환을 완료하지 않았을 경우에는 바꿀 수 있는 모든 경우의 수를 고려
    for i in range(len(cards)-1):
        # i 는 교환하려고 하는 카드
        for j in range(i+1,len(cards)):
            # j는 교환 대상 카드
            cards[i], cards[j] = cards[j], cards[i]
            solve(cnt+1)
            # 원래 모양으로 돌려놓고 다음 교환 시도
            cards[i], cards[j] = cards[j], cards[i]
    pass


T = int(input())
for tc in range(1,T+1):
    # 모든 경우의 수를 다 고려할 것
    # 교환 횟수와 값이 같은 경우는 두번 계산하지 않는다.
    cards, N = input().split()
    cards = list(cards)
    N = int(N)
    check = set ()              # 만들었던 case 를 저장하는 set
