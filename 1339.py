# 아래 코드는 ChatGPT가 자동으로 생성한 코드입니다.
# 문제 정보: 1339

words = []  # 단어를 담을 리스트
freq = {}  # 알파벳 빈도수를 담을 딕셔너리

# 입력 받기
n = int(input())
for i in range(n):
    words.append(input())

# 알파벳 빈도수 계산
for word in words:
    for i in range(len(word)):
        alpha = word[i]
        freq[alpha] = freq.get(alpha, 0) + 10**(len(word)-i-1)

# 빈도수를 내림차순으로 정렬하여 숫자 할당
num = 9
for key, value in sorted(freq.items(), key=lambda x:x[1], reverse=True):
    freq[key] = num
    num -= 1

# 각 단어의 값 계산하여 더하기
result = 0
for word in words:
    temp = ""
    for alpha in word:
        temp += str(freq[alpha])
    result += int(temp)

# 결과 출력
print(result)