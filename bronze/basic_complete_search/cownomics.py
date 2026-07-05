n, k = map(int, input().split())
spotty = []
plain = []
for i in range(n*2):
  s = input()
  if i < n:
    spotty.append(s)
  else:
    plain.append(s)
count = 0
for p in range(k):
  spotty_set = spotty_set = {spotty[j][p] for j in range(n)}
  plain_set = plain_set = {plain[z][p] for z in range(n)}
  if spotty_set.isdisjoint(plain_set):
    count += 1
print(count)