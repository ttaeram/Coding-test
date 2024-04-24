import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    M, N, x, y = map(int, input().split())
    flag = True
    while x <= M * N:
        if (x - y) % N == 0:
            ans = x
            flag = False
            break
        x += M
    if flag:
        ans = -1
    print(ans)