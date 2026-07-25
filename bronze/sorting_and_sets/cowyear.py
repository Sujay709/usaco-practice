zodiac = ["Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat"]
cows = {"Bessie": 0}
n = int(input())
for i in range(n):
  phrase = input().split()
  cow1, rel, animal, cow2 = [phrase[i] for i in [0, 3, 4, -1]]
  if rel == "previous":
    year = cows[cow2] - 1
    while zodiac[year % 12] != animal:
      year -= 1
  else:
    year = cows[cow2] + 1
    while zodiac[year % 12] != animal:
      year += 1
  cows[cow1] = year
print(abs(cows["Elsie"]))