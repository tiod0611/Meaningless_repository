# 아래 코드는 ChatGPT가 자동으로 생성한 코드입니다.
# 문제 정보: 1213

s = input()
s_counts = [0] * 26

# 알파벳 개수 카운트
for i in s:
    s_counts[ord(i) - 65] += 1

odd_count = 0
odd_index = -1
result = ""

# 팰린드롬 만들기
for i in range(26):
    if s_counts[i] % 2 == 1:
        odd_count += 1
        odd_index = i
        if odd_count > 1:
            print("I'm Sorry Hansoo")
            exit(0)
    result += chr(i + 65) * (s_counts[i] // 2)

# 결과 출력
if odd_count == 1:
    print(result + chr(odd_index + 65) + result[::-1])
else:
    print(result + result[::-1])