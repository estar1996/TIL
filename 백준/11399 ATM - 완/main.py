import sys
sys.stdin = open("input.txt")

N = int(input())
line = list(map(int,input().split()))

n_line = sorted(line)

cnt = 0
for i in range(len(n_line)+1):
    cnt += sum(n_line[0:i])
print(cnt)