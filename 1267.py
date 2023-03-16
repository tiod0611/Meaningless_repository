# 아래 코드는 ChatGPT가 자동으로 생성한 코드입니다.
# 문제 정보: 1267

N = int(input())
calls = list(map(int, input().split()))

y_total = 0
m_total = 0

for call in calls:
    y_total += ((call // 30) + 1) * 10
    m_total += ((call // 60) + 1) * 15

if y_total < m_total:
    print("Y", y_total)
elif m_total < y_total:
    print("M", m_total)
else:
    print("Y M", m_total)