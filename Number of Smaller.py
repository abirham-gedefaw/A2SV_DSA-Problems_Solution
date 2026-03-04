n, m = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

first = 0
result = []

for second in range(m):
  while first < len(list1) and list1[first] < list2[second]:
    first += 1
  result.append(first)
print(" ".join(map(str, result)))
