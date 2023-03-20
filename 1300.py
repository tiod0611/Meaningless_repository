# 아래 코드는 ChatGPT가 자동으로 생성한 코드입니다.
# 문제 정보: 1300n = int(input())
k = int(input())

start, end = 1, k
result = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(1, n+1):
        cnt += min(mid//i, n)
    if cnt >= k:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)