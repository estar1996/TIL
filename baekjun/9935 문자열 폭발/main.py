import sys
sys.stdin = open('input.txt')

string = input()
bomb = input()

bomb_last = bomb[-1]
N = len(bomb)
stack = []

for i in string:
    stack.append(i)
    if i == bomb_last and ''.join(stack[-N:]) == bomb:
        del stack[-N:]
res = ''.join(stack)

if len(res) == 0:
    print("FRULA")
else:
    print(res)
