string = input()
bomb = list(map(str, input().strip()))
stack = []

for i in range(len(string)):
    stack.append(string[i])

    if stack[len(stack) - len(bomb) : len(stack)] == bomb:
        for j in range(len(bomb)):
            stack.pop()

if stack:
    print(*stack, sep = '')
else:
    print('FRULA')