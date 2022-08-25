import sys
sys.stdin = open("sample_input(1).txt")

T = int(input())

for tc in range(1,T+1):
    string = list(map(str,input()))
    stack = [0]
    res = 1
    

    for i in string:
        if i in ('(','{'):
            stack.append(i)
            

        elif i in (')','}'): 
            if i == ')':
                if stack[-1] == '(':
                    stack.pop()
                elif stack[-1] == 0:
                    res = 0
                    break
                else :
                    res = 0
                    break    
            elif i =='}':
                if stack[-1] == '{':
                    stack.pop()
                elif stack[-1] == 0:
                    res = 0
                    break
                else :
                    res = 0
                    break
            
            else :
                res = 0
                break
        
        
    print("#{} {}".format(tc,res))
    print(stack)