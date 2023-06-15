import sys
import heapq

T = int(input())
h = []
for _ in range(1,T+1):
    n = int(sys.stdin.readline())
    if n != 0:
        heapq.heappush(h,(-n))
    else:
        try:
            print(-1 * heapq.heappop((h)))
        except:
            print(0)

