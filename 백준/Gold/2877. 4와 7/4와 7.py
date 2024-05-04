import sys
input = sys.stdin.readline

K = int(input())
ans = ''
while K > 0:
    if K % 2 == 0:
        ans = '7' + ans
        K -= 2
    else:
        ans = '4' + ans
    K = K // 2
print(ans)