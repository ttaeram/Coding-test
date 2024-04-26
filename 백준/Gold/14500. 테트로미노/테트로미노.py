import sys
input = sys.stdin.readline

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def dfs(cur, cnt, temp):
    global ans
    if temp + max_v*(4-cnt) <= ans:
        return
    if cnt == 4:
        ans = max(ans, temp)
        return
    for cR, cC in cur:
        for k in range(4):
            nR, nC = cR+dr[k], cC+dc[k]
            if 0 <= nR < nr and 0 <= nC < nc and not v[nR][nC]:
                v[nR][nC] = 1
                dfs(cur+[(nR, nC)], cnt+1, temp+arr[nR][nC])
                v[nR][nC] = 0

nr, nc = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(nr)]

v = [[0] * nc for _ in range(nr)]
ans = 0
max_v = max(map(max, arr))
for r in range(nr):
    for c in range(nc):
        v[r][c] = 1
        dfs([(r, c)], 1, arr[r][c])
        # v[r][c] = 0   # (r, c)를 포함하는 모든 모양 검사 완료해서 v[r][c]를 0으로 되돌릴 필요 X
print(ans)