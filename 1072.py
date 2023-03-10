import math

x, y = map(int, input().split())

# 이긴 게임 수 계산
win = math.floor(y * 100 / x)

# 승률이 변하지 않을 경우
if win >= 99:
    print(-1)
else:
    left, right = 0, 1000000000
    answer = -1
    while left <= right:
        mid = (left + right) // 2
        # 횟수가 mid번만큼 더 진행했을 때 승률 계산
        temp_win = math.floor((y + mid) * 100 / (x + mid))
        # 이전 승률보다 높아졌다면
        if temp_win > win:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    print(answer)