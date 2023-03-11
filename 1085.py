# 아래 코드는 ChatGPT가 자동으로 생성한 코드입니다.# 문제 정보: 1085x, y, w, h = map(int, input().split())

distance_x = min(x, w-x)
distance_y = min(y, h-y)

print(min(distance_x, distance_y))