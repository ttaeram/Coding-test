N = int(input())

rope = []
for i in range(N):
    rope.append(int(input()))
s_rope = sorted(rope, reverse=True)

max_rope = 0
for ind, ro in enumerate(s_rope):
    if ro * (ind + 1) > max_rope:
        max_rope = ro * (ind + 1)

print(max_rope)