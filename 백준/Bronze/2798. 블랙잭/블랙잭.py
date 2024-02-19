N, M = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            sum_cards = cards[i] + cards[j] + cards[k]
            if max_sum < sum_cards <= M:
                max_sum = sum_cards

print(max_sum)