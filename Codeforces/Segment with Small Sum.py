n, s = map(int, input().split())
array = list(map(int, input().split()))
longest_segment = 0
total = 0
left = 0
for right in range(len(array)):
  total += array[right]
  while total > s:
    total -= array[left]
    left += 1
  
  longest_segment = max(right - left + 1, longest_segment)
  
print(longest_segment)
