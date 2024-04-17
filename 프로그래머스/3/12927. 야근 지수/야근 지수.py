import heapq
def solution(n, works):
    if n >= sum(works):
        ans = 0
        return ans
    
    heap = []
    for w in works:
        heapq.heappush(heap, (-w, w))
    for t in range(n):
        work = heapq.heappop(heap)[1]
        work -= 1
        heapq.heappush(heap, (-1 * work, work))

    # works.sort()
    # for _ in range(n):
    #     works[-1] -= 1
    #     works.sort()
    ans = 0
    for w in heap:
        ans += w[1] ** 2
    return ans