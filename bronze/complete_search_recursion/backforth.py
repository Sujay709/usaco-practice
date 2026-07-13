def solve(day, barn1_tank, barn1_counts, total_counts, results):
  if day > 4:
    results.add(barn1_tank)
    return
  pulling_from_barn1 = (day == 1 or day == 3)
  sign =  -1 if pulling_from_barn1 else +1

  for size in range(1, 101):
    if pulling_from_barn1:
      available = barn1_counts[size] > 0
    else:
      barn2_count = total_counts[size] - barn1_counts[size]
      available = barn2_count > 0
    
    if available:
      if pulling_from_barn1:
        barn1_counts[size] -= 1
      else:
        barn1_counts[size] += 1
      new_barn1_tank = barn1_tank + sign * size
      solve(day + 1, new_barn1_tank, barn1_counts, total_counts, results)
      if pulling_from_barn1:
        barn1_counts[size] +=1
      else:
        barn1_counts[size] -= 1
def main():
  barn1_sizes = list(map(int, input().split()))
  barn2_sizes = list(map(int, input().split()))
  total_counts = [0]*101
  barn1_counts = [0]*101
  for s in barn1_sizes + barn2_sizes:
    total_counts[s] += 1
  for s in barn1_sizes:
    barn1_counts[s] += 1
  
  results = set()
  solve(1, 1000, barn1_counts, total_counts, results)
  print(len(results))

main()