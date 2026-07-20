n = int(input())
prices = list(map(int, input().split()))
prices.sort()
max_profit = 0
best_price = 0
for i in range(n):
  price = prices[i]
  count = n - i
  profit = price * count
  if profit > max_profit:
    max_profit = profit
    best_price = price

print(max_profit, best_price)
