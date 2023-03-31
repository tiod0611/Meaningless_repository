# 아래 코드는 ChatGPT가 자동으로 생성한 코드입니다.
# 문제 정보: 1373num = input()
if len(num) % 3 == 1:
    num = '00' + num
elif len(num) % 3 == 2:
    num = '0' + num
 
result = ''
for i in range(0, len(num), 3):
    result += str(int(num[i:i+3], 2))
    
print(result)