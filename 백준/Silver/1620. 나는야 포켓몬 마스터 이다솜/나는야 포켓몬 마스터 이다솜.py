import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}

for i in range(1, N + 1):
    n = input().strip()
    dic[i] = n
    dic[n] = i

for m in range(M):
    q = input().strip()
    if q.isalpha():
        print(dic[q])
    else:
        print(dic[int(q)])