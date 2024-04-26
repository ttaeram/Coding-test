import sys
input = sys.stdin.readline

from heapq import heappop, heappush

g = [[] for _ in range(101)]
n, m = map(int, input().rstrip().split())
for _ in range(n+m):
    k1, k2 = map(int, input().rstrip().split())
    g[k1].append((0, k2))
for i in range(101):
    if not g[i]:
        g[i].extend([(1, i+k) for k in range(1, min(7, 101-i))])

d = [float('inf')]*101
q = [(0, 1)]
while q:
    cw, cp = heappop(q)
    if cp != 100 and d[cp] >= cw:
        for nw, np in g[cp]:
            nw += cw
            if d[np] > nw:
                d[np] = nw
                heappush(q, (nw, np))
print(d[100])