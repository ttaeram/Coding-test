def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)

    ans = 0
    a = 0
    b = 0
    while a < len(A):
        if A[a] < B[b]:
            ans += 1
            b += 1
        a += 1
    return ans