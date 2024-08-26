def solution(scores):
    me_a, me_b = scores[0]
    me_total = me_a + me_b
    max_b = 0
    result = []
    scores.sort(key=lambda x : (-x[0], x[1]))
    
    ans = 0
    for score in scores:
        a, b = score
        if a > me_a and b > me_b:
            return -1
        
        if b >= max_b:
            max_b = b
        else:
            continue
            
        if a + b > me_total:
            ans += 1
    
    return ans + 1
