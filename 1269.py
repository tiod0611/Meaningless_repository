# 아래 코드는 ChatGPT가 자동으로 생성한 코드입니다.
# 문제 정보: 1269a_len, b_len = map(int, input().split())
a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))

sym_diff = a_set.symmetric_difference(b_set)
print(len(sym_diff))