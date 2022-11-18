import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
checks = list(map(int, sys.stdin.readline().split()))

res = [0] * (M+1)

cards_set = set(cards)
checks_set = set(checks)



# print(res)



