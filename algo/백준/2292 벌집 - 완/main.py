import sys
sys.stdin = open("input.txt")



cnt = 1
num = int(input())
res = 1
while res < num:
    res += cnt*6
    cnt += 1
print(cnt)