n = int(input())
cows = list(map(int, input().split()))

evens = len([a for a in cows if a % 2 == 0])
odds = len([b for b in cows if b % 2 == 1])
while odds > evens:
  odds -= 2
  evens += 1

if evens > odds + 1:
  evens = odds + 1

print(evens + odds)