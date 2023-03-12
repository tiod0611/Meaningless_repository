# 아래 코드는 ChatGPT가 자동으로 생성한 코드입니다.
# 문제 정보: 1100

board = []
count = 0

for i in range(8):
    board.append(input())

for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0 and board[i][j] == 'F':
            count += 1

print(count)