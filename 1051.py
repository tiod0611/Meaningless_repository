

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)] # 입력받은 배열

max_len = min(n, m) # 정사각형이 될 수 있는 가장 큰 크기

for k in range(max_len, 0, -1): # 큰 크기부터 작아지는 순서로 확인
    for i in range(n-k+1):
        for j in range(m-k+1):
            if arr[i][j] == arr[i+k-1][j] == arr[i][j+k-1] == arr[i+k-1][j+k-1]:
                print(k*k)
                exit() # 찾았으면 프로그램 종료

# 정사각형을 찾지 못했을 경우
print(1)