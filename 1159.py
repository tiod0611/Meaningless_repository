# 아래 코드는 ChatGPT가 자동으로 생성한 코드입니다.
# 문제 정보: 1159

players = [] # 선수들의 이름을 저장할 빈 리스트

for i in range(int(input())):
    name = input()
    players.append(name[0]) # 각 선수의 성만 리스트에 저장

result = ''
for alpha in set(players): # 중복을 제거한 각 알파벳마다 반복
    if players.count(alpha) >= 5: # 해당 알파벳이 출전 선수 5명 이상일 경우
        result += alpha

if not result: # 출전 선수 5명 이상인 알파벳이 없을 경우
    print('PREDAJA')
else:
    print(''.join(sorted(result))) # 알파벳 순으로 정렬하여 출력