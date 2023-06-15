import sys
sys.stdin = open('input.txt')

N = int(input())
lst = []
for _ in range(N):
    l = int(input())
    lst.append(l)

lst.sort()

result = []
for i in range(len(lst)):
    result.append(lst[i] * (len(lst)-i))
print(max(result))

