import sys
input = sys.stdin.readline
import heapq

N = int(input())
lst = []
for _ in range(N):
    heapq.heappush(lst,int(sys.stdin.readline()))

if len(lst) == 1:
    print(0)
else:
    res = 0
    while len(lst) > 1:
        min_c = heapq.heappop(lst)
        min_c2 = heapq.heappop(lst)
        res += min_c + min_c2
        heapq.heappush(lst,min_c + min_c2)
    print(res)
