q = int(input())
dictionary = dict()
for _ in range(q):
  line = list(map(int, input().strip().split()))
  if not line[0]:
    dictionary.update({line[1]:line[2]})
  else:
    try:
      print(dictionary[line[1]])
    except KeyError:
      print(0)
