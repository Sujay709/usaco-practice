milk_totals = {
  "Bessie": 0, 
  "Elsie": 0, 
  "Daisy": 0, 
  "Gertie": 0,
  "Annabelle": 0, 
  "Maggie": 0, 
  "Henrietta": 0
}

n = int(input())
for _ in range(n):
  name, amt = input().split()
  amt = int(amt)
  milk_totals[name] += amt
unique_amounts = sorted(list(set(milk_totals.values())))
if len(unique_amounts) < 2:
  print("Tie")
else:
  target_amounts = unique_amounts[1]
  winning_cows = []
  for cow, amount in milk_totals.items():
    if amount == target_amounts:
      winning_cows.append(cow)
  if len(winning_cows) == 1:
    print(winning_cows[0])
  else:
    print("Tie")