n = int(input())
a = list(map(int, input().split()))

first_seen = {}

last_position = {}
second_last_position = {}

distinct_so_far = [0] * (n + 1)
seen_before = set()
count_of_distinct = 0

for i in range(n):
  num = a[i]
  if num not in seen_before:
    seen_before.add(num)
    count_of_distinct += 1
    first_seen[num] = i

  distinct_so_far[i + 1] = count_of_distinct

  if num in last_position:
    second_last_position[num] = last_position[num]
  last_position[num] = i

total = 0

for num in second_last_position:
  spot = second_last_position[num]
  choices = distinct_so_far[spot]
  if first_seen[num] < spot:
    choices -= 1
  total += choices

print(total)