import sys
input = sys.stdin.readline

def sol():
    N = int(input())
    arr = []
    ans = 0
    for _ in range(N):
        a, b = map(int, input().split())
        arr.append((a, b))
        
    arr.sort(key=lambda x: x[0])
    stack = []
    for idx in range(N):
        a, b = arr[idx]
        if not stack:
            ans += 1
            stack.append(b)
        else:
            flag = True
            for i in range(len(stack)):
                if stack[i] <= a:
                    stack[i] = b
                    flag = False
                    break
            if flag:
                ans += 1
                stack.append(b)
    print(ans)
sol()