# 아래 코드는 ChatGPT가 자동으로 생성한 코드입니다.
# 문제 정보: 1182

from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
for i in range(1, n+1):
    subset = combinations(arr, i)
    for j in subset:
        if sum(j) == s:
            count += 1

print(count)