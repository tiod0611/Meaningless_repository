# 아래 코드는 ChatGPT가 자동으로 생성한 코드입니다.
# 문제 정보: 1292

nums = list(map(int, input().split()))
arr = []
for i in range(nums[1]):
    for j in range(i+1):
        arr.append(i+1)
print(sum(arr[nums[0]-1:nums[1]]))