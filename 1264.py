# 아래 코드는 ChatGPT가 자동으로 생성한 코드입니다.
# 문제 정보: 1264while True:
    sentence = input().lower()
    if sentence == '#':
        break
    count = 0
    for letter in sentence:
        if letter in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    print(count)