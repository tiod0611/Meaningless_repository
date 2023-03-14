# 아래 코드는 ChatGPT가 자동으로 생성한 코드입니다.
# 문제 정보: 1244switch_count = int(input())
switch_state = list(map(int, input().split()))
student_count = int(input())

for i in range(student_count):
    gender, num = map(int, input().split())
    if gender == 1:
        for j in range(num-1, switch_count, num):
            switch_state[j] = 1 - switch_state[j]
    else:
        num -= 1
        switch_state[num] = 1 - switch_state[num]
        for j in range(1, min(num+1, switch_count - num)):
            if switch_state[num-j] == switch_state[num+j]:
                switch_state[num-j] = 1 - switch_state[num-j]
                switch_state[num+j] = 1 - switch_state[num+j]
            else:
                break

for i in range(0, switch_count, 20):
    print(*switch_state[i:i+20])