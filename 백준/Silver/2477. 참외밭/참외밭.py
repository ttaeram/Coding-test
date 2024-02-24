N = int(input())
arr = []
x = []
y = []
res = []

for _ in range(6):
    a, b = map(int, input().split())
    arr.append([a, b])
    if a == 1 or a == 2:
        x.append(b)
    if a == 3 or a == 4:
        y.append(b)

for i in range(6):
    if arr[i][0] == arr[(i+2)%6][0]:
        res.append(arr[(i + 1) % 6][1])

ans = (max(x) * max(y) - res[0] * res[1]) * N

print(ans)