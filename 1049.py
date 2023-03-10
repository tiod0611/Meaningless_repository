import sys

n, m = map(int, sys.stdin.readline().split())
pack_price = []
unit_price = []

for i in range(m):
    pack, unit = map(int, sys.stdin.readline().split())
    pack_price.append(pack)
    unit_price.append(unit)

min_pack = min(pack_price)
min_unit = min(unit_price)

if min_pack <= min_unit * 6:
    total = (n // 6) * min_pack
    if (n % 6) * min_unit < min_pack:
        total += (n % 6) * min_unit
    else:
        total += min_pack
else:
    total = n * min_unit

print(total)