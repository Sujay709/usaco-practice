n = int(input())
if n == 1:
  print("1")
elif n == 2 or n == 3:
  print("NO SOLUTION")
elif n == 4:
  print("2 4 1 3")
else:
  results = []
  for x in range(1, n+1, 2):
    results.append(str(x))
  for x in range(2, n+1, 2):
    results.append(str(x))
  print(" ".join(results))