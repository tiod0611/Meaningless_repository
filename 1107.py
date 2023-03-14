# 아래 코드는 ChatGPT가 자동으로 생성한 코드입니다.
# 문제 정보: 1107

# 조합을 이용한 풀이

import itertools

channels = set(range(0, 10)) # 채널은 0부터 9까지의 숫자로 이루어짐

def possible(channel, buttons):
    for digit in str(channel):
        if int(digit) not in buttons:
            return False
    return True

n = int(input())
m = int(input())
broken = set()
if m > 0:
    broken = set(map(int, input().split()))
    
result = abs(n - 100) # 초기값 = n에서 100까지 +,- 버튼만 이용해서 가는 경우

# 채널을 하나씩 만들어가며 가장 가까운 채널을 찾는다.
for channel in range(1000001):
    # 채널의 각 자릿수가 고장난 경우는 스킵
    if not possible(channel, channels - broken):
        continue
    
    # 해당 채널에서 목표 채널까지 +,- 버튼만 이용해서 이동하는 횟수
    count = abs(n - channel)
    
    # 결과 갱신
    if count + len(str(channel)) < result:
        result = count + len(str(channel))
        
print(result)