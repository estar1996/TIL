import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1,T+1):
    N, M, L = map(int,input().split())
    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)
    for _ in range(M):
        node = list(map(int,input().split()))
        ch1[int(node[0])] = node[1]
        ch2[int(node[0])] = 1


    for i in range(1,len(ch2)+1):
        if ch2[len(ch2)-i] == 1:
            pass
        elif ch2[len(ch2)-i] == 0:
            if (len(ch2)-i) * 2 <= len(ch2)-1:
                ch1[len(ch2)-i] += ch1[(len(ch2)-i) * 2]
            if (len(ch2)-i) * 2 +1 <= len(ch2)-1:
                ch1[len(ch2) - i] += ch1[(len(ch2) - i) * 2 + 1]
    print("#{} {}".format(tc,ch1[L]))
    # for i in range(1,N//2+1):
    #     print(-i)
