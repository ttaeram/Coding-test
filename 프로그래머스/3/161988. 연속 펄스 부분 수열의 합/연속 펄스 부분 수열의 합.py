def solution(sequence):
    arr = [(0, 0)] * (len(sequence))
    arr[0] = (sequence[0], -1 * sequence[0])
        
    for i in range(1, len(sequence)):
        if i % 2 == 0:
            arr[i] = (max(sequence[i], arr[i-1][0] + sequence[i]), max(-1 * sequence[i], arr[i-1][1] - sequence[i]))
        else:
            arr[i] = (max(-1 * sequence[i], arr[i-1][0] - sequence[i]), max(sequence[i], arr[i-1][1] + sequence[i]))
    
    ans = 0
    for i in range(len(sequence)):
        ans = max(ans, arr[i][0], arr[i][1])
            
    return ans