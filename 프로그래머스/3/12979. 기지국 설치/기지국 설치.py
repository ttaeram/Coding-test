def solution(n, stations, w):
    cnt = 1
    ans = 0
    dif = 2 * w + 1
    for s in stations:
        if s - w - cnt > 0:
            ans += (s - w - cnt)//dif
            if (s - w - cnt) % dif: 
                ans += 1
        cnt = s + w + 1
    if n - cnt + 1 > 0:
        ans += (n - cnt + 1) // dif
        if (n - cnt + 1) % dif:
            ans += 1
    return ans