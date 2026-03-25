n , t = map(int, input().split())
books = list(map(int, input().split()))

books_read = 0
total_time = 0
left = 0
for right in range (len(books)):
  total_time += books[right]
  while total_time > t:
    total_time -= books[left]
    left += 1
  books_read = max(books_read, right - left + 1)

print(books_read)
