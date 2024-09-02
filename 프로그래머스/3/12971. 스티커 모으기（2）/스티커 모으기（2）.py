def solution(sticker):
    N = len(sticker)
    ans = 0
    dp = [(0, 0)] * N
    if N <= 2:
        ans = max(sticker)
        return ans
    else:
        dp[0] = (sticker[0], 0)
        dp[1] = (0, sticker[1])
        dp[2] = (sticker[2] + sticker[0], sticker[2])

        for i in range(3, N):
            a = max(sticker[i] + dp[i-2][0], sticker[i] + dp[i-3][0])
            b = max(sticker[i] + dp[i-2][1], sticker[i] + dp[i-3][1])
            dp[i] = (a, b)

        ans = max(dp[-1][1], dp[-2][0], dp[-2][1], dp[-3][0])
        return ans
