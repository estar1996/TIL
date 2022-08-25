
import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1,T+1):
    N =int(input())
    lst = [0]*(N//10)
    
    for i in range(N//10):
        if i == 0:
            lst[i] = 1
        elif i == 1:
            lst[i] = 3
        elif i >= 2:
            lst[i] = lst[i-1] + 2*lst[i-2]
            

    print(f"#{tc} {lst.pop()}")



# 10 - 1
# 20 - 3
# 30 - 5
# 40 - 11
# 50 - 21
# 60 - 43
# 70 - 85

