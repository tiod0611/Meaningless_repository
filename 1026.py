a_len = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort()

result = 0
for i in range(a_len):
    result += a[i] * b[i]

print(result)