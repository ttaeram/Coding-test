import sys
input = sys.stdin.readline

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

x_list = []
y_list = []

for i in range(w):
    x_list.append(i)
for j in range(w, 0, -1):
    x_list.append(j)

for k in range(h):
    y_list.append(k)
for l in range(h, 0, -1):
    y_list.append(l)

x = x_list[(p + t) % (2 * w)]
y = y_list[(q + t) % (2 * h)]

print(x, y)