import sys
input = sys.stdin.readline

A, B = map(int, input().split())

ans = 1
while B != A:
    ans += 1
    res = B
    if B % 10 == 1:
        B //= 10
    elif B % 2 == 0:
        B //= 2
    
    if res == B:
        print(-1)
        break
else:
    print(ans)