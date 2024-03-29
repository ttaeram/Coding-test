import sys
input = sys.stdin.readline

N = int(input())
col_dict = {}
for _ in range(N):
    x, y = map(int, input().split())
    col_dict[x] = y

x_list = sorted(col_dict.keys())

S = 0
max_i = 0
for l in x_list:
    if col_dict[l] == max(col_dict.values()):
        max_i = l

h = col_dict[x_list[0]]

for i in range(x_list.index(max_i)):
    if h < col_dict[x_list[i + 1]]:
        S += (x_list[i + 1] - x_list[i]) * h
        h = col_dict[x_list[i + 1]]
    else:
        S += (x_list[i + 1] - x_list[i]) * h

h = col_dict[x_list[-1]]

for i in range(N - 1, x_list.index(max_i), -1):
    if h < col_dict[x_list[i - 1]]:
        S += (x_list[i] - x_list[i - 1]) * h
        h = col_dict[x_list[i - 1]]
    else:
        S += (x_list[i] - x_list[i - 1]) * h
S += col_dict[max_i]
print(S)