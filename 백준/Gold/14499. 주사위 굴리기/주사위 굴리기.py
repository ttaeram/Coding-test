import sys
input = sys.stdin.readline

# 방향 설정 (동, 서, 북, 남)
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

# 주사위 초기 상태
dice = {
    'top': 0,
    'bottom': 0,
    'left': 0,
    'right': 0,
    'front': 0,
    'back': 0
}

def roll_east(dice):
    return {
        'top': dice['left'],
        'bottom': dice['right'],
        'left': dice['bottom'],
        'right': dice['top'],
        'front': dice['front'],
        'back': dice['back']
    }

def roll_west(dice):
    return {
        'top': dice['right'],
        'bottom': dice['left'],
        'left': dice['top'],
        'right': dice['bottom'],
        'front': dice['front'],
        'back': dice['back']
    }

def roll_north(dice):
    return {
        'top': dice['front'],
        'bottom': dice['back'],
        'left': dice['left'],
        'right': dice['right'],
        'front': dice['bottom'],
        'back': dice['top']
    }

def roll_south(dice):
    return {
        'top': dice['back'],
        'bottom': dice['front'],
        'left': dice['left'],
        'right': dice['right'],
        'front': dice['top'],
        'back': dice['bottom']
    }

for command in commands:
    dx, dy = directions[command - 1]
    nx, ny = x + dx, y + dy

    if 0 <= nx < N and 0 <= ny < M:
        x, y = nx, ny

        if command == 1:  # 동쪽
            dice = roll_east(dice)
        elif command == 2:  # 서쪽
            dice = roll_west(dice)
        elif command == 3:  # 북쪽
            dice = roll_north(dice)
        elif command == 4:  # 남쪽
            dice = roll_south(dice)

        if arr[x][y] == 0:
            arr[x][y] = dice['bottom']
        else:
            dice['bottom'] = arr[x][y]
            arr[x][y] = 0

        print(dice['top'])
