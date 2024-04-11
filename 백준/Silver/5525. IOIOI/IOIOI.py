import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()
s = 'I'
for _ in range(N):
    s += 'OI'
cnt = 0
for m in range(M):
    if S[m:m + (2 * N + 1)] == s:
        cnt += 1
print(cnt)