import sys
input = sys.stdin.readline

N = int(input())
stack = []

for n in range(N):
    command = input().rstrip()
    if 'push' in command:
        a = int(command[5:])
        stack.append(a)
    
    elif command == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    
    elif command == 'size':
        print(len(stack))
    
    elif command == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    
    elif command == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)