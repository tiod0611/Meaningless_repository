

N = int(input())
F = int(input())

N //= 100
N *= 100

while N % F != 0:
    N += 1

print(str(N)[-2:])