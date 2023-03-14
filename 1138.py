# 아래 코드는 ChatGPT가 자동으로 생성한 코드입니다.
# 문제 정보: 1138

n = int(input())
heights = list(map(int, input().split()))
line = [0 for _ in range(n)]

for i in range(n):
    cnt = heights[i]
    for j in range(n):
        if cnt == 0 and line[j] == 0:
            line[j] = i+1
            break
        elif line[j] == 0:
            cnt -= 1
        
for h in line:
    print(h, end=' ')