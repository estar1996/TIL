import sys
sys.stdin = open("input.txt")

N = int(sys.stdin.readline())
cards = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
checks = list(map(int, sys.stdin.readline().split()))

res = [0] * (len(checks))

for i in range(len(checks)):
    if checks[i] in cards:
        res[i] = 1
for k in res:
    print(k)
