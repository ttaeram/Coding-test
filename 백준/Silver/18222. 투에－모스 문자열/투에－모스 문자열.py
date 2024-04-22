import sys
input = sys.stdin.readline

k = int(input())

def sol(k):
    if k == 0:
        return 0
    if k == 1:
        return 1
    if k % 2 == 0:
        return sol(k // 2)
    else:
        return 1 - sol(k // 2)

ans = sol(k - 1)
print(ans)