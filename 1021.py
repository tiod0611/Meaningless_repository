

from collections import deque

n, m = map(int, input().split())
target = deque(map(int, input().split()))
queue = deque([i for i in range(1, n+1)])
count = 0

while target:
    if target[0] == queue[0]:
        target.popleft()
        queue.popleft()
    else:
        if queue.index(target[0]) <= len(queue)//2:
            while target[0] != queue[0]:
                queue.append(queue.popleft())
                count += 1
        else:
            while target[0] != queue[0]:
                queue.appendleft(queue.pop())
                count += 1

print(count)