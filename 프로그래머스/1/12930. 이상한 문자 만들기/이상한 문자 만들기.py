def solution(s):
    arr = list(map(str, s.split(" ")))
    for i in range(len(arr)):
        arr[i] = list(arr[i])
        for j in range(len(arr[i])):
            if j % 2 == 0:
                arr[i][j] = arr[i][j].upper()
            else:
                arr[i][j] = arr[i][j].lower()
        arr[i] = ''.join(arr[i])
    answer = ' '.join(arr)
    # if answer[-1] == ' ':
    #     answer = answer[:-1]
    return answer