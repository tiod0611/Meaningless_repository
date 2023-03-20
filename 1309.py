# 아래 코드는 ChatGPT가 자동으로 생성한 코드입니다.
# 문제 정보: 1309

n = int(input())
dp = [1, 3] + [0] * (n-1)

for i in range(2, n+1):
    dp[i] = (dp[i-1] * 2 + dp[i-2]) % 9901

print(dp[n])