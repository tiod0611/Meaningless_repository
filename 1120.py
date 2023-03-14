# 아래 코드는 ChatGPT가 자동으로 생성한 코드입니다.
# 문제 정보: 1120a, b = input().split()

min_diff = len(b)
for i in range(len(b) - len(a) + 1):
    diff = sum(1 for x, y in zip(a, b[i:i+len(a)]) if x != y)
    if diff < min_diff:
        min_diff = diff

print(min_diff)