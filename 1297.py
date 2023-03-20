# 아래 코드는 ChatGPT가 자동으로 생성한 코드입니다.
# 문제 정보: 1297

import math

diagonal, height_ratio, width_ratio = map(int, input().split())

height = height_ratio * diagonal / math.sqrt(height_ratio**2 + width_ratio**2)
width = width_ratio * diagonal / math.sqrt(height_ratio**2 + width_ratio**2)

print(int(height), int(width))