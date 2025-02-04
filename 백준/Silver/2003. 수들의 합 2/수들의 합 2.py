import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

def sol():
    ans = 0

    for i in range(N):
        res = 0

        for j in range(i, N):
            res += arr[j]

            if res == M:
                ans += 1
                break

            if res > M:
                break
    
    return ans

ans = sol()
print(ans)