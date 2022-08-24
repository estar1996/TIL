import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1,T+1):
    L = list(input())
    cnt = 0
    stick = 0
    for i in range(0,len(L)):
        if L[i] == '(' and L[i+1] == ')':
            cnt += stick
            i += 2
        elif L[i] == '(' :
            stick += 1
        else :
            stick -= 1

    print(tc,cnt)