# 아래 코드는 ChatGPT가 자동으로 생성한 코드입니다.
# 문제 정보: 1302books = {}
n = int(input())

for i in range(n):
    book = input()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

max_count = max(books.values())
best_seller = []

for book, count in books.items():
    if count == max_count:
        best_seller.append(book)

best_seller.sort()
print(best_seller[0])