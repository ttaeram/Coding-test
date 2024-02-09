N,M =map(int,input().split())
board = []

for _ in range(N):
    board.append(list(input()))
c = 0
for i in range(N-7):
    for j in range(M-7):
        black = 0
        for a in range(8):
            for b in range(8):
                if (a+b) %2 ==0:
                    black += (board[a+i][b+j]=="B")
                else:
                    black += (board[a+i][b+j]=="W")    
        if black < 32:
            black = 64 - black
        if c < black:
            c=black
print(64-c)