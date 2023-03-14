# 아래 코드는 ChatGPT가 자동으로 생성한 코드입니다.
# 문제 정보: 1181

import sys

n = int(sys.stdin.readline())
words = []
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    length = len(word)
    words.append((length, word))
words = list(set(words))
words.sort(key = lambda x: (x[0], x[1]))

for length, word in words:
    print(word)