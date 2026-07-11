cows = []
air_conditioners = []
min_cost = float("inf")
def check():
  global min_cost
  possible = True
  for i in range(1, 101):
    cooling = 0
    for j in range(M):
      if not uses[j]:
        continue
      a,b,p,m = air_conditioners[j]
      if a <= i <= b:
        cooling += p
    cow_req = 0
    for s,t,c in cows:
      if s <= i <= t:
        cow_req = c
        break
    if cooling < cow_req:
      possible = False
      break

  if possible:
    cost = sum(air_conditioners[i][3] for i in range(M) if uses[i])
    min_cost = min(min_cost, cost)

def search(i: int):
  if i == M:
      check()
  else:
    uses[i] = False
    search(i + 1)
    uses[i] = True
    search(i + 1)

N, M = map(int, input().split())
uses = [False] * M
for _ in range(N):
	s, t, c = map(int, input().split())
	cows.append((s, t, c))

for _ in range(M):
  a, b, p, m = map(int, input().split())
  air_conditioners.append((a, b, p, m))

search(0)
print(min_cost)