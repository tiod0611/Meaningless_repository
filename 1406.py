# 아래 코드는 ChatGPT가 자동으로 생성한 코드입니다.
# 문제 정보: 1406
import sys
from collections import deque

input = sys.stdin.readline

left_stack = deque(input().strip())
right_stack = deque()

n = int(input())

for _ in range(n):
    command = input().strip()

    if command == "L":
        if left_stack:
            right_stack.appendleft(left_stack.pop())

    elif command == "D":
        if right_stack:
            left_stack.append(right_stack.popleft())

    elif command == "B":
        if left_stack:
            left_stack.pop()

    else:
        left_stack.append(command.split()[1])

print("".join(left_stack + right_stack))