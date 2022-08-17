import sys
sys.stdin = open("sample_input(1).txt")

T = int(input())

for tc in range(1,T+1):
    string = list(map(str,input()))
    stack = []
    res = 1
    result =0
    for i in string:
        if i in ('(','{'):
            stack.append(i)
        elif i in(')','}'):
            if i ==')' and stack.pop() =='(':
                res = 0
            elif i =='}' and stack.pop() == '{':
                res = 0
            elif len(stack) == 0:
                res = 0
        if len(stack) == 0:
            result = 1
        else :
            result = 0
    
    
    
    print("#{} {}".format(tc,result))
    # print(stack)