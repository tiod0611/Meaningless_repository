

n = int(input()) # 양의 정수 개수 입력 받기
divisors = list(map(int, input().split())) # 약수 리스트 입력 받기

max_divisor = max(divisors) # 약수 리스트에서 최댓값을 구함
min_divisor = min(divisors) # 약수 리스트에서 최솟값을 구함

print(max_divisor * min_divisor) # 최댓값과 최솟값을 곱한 값을 출력