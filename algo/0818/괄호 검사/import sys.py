import sys
sys.stdin = open("sample_input(1).txt")

T = int(input())
for tc in range(1, T+1):
    S = input()
 
    stack = [None] * len(S)
    top = -1
    dic = {')': '(', '}': '{'}
    for i in S:
        if '(' == i or '{' == i:
            stack[top + 1] = i
            top += 1
        elif ')' == i or '}' == i:
            if stack[top] == dic[i]:
                stack.pop(top)
                top -= 1
            else:
                top += 1
                break
    if top == -1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')

    print(stack)