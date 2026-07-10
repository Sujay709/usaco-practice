from itertools import permutations

n = input()
perms = set(permutations(n))
print(len(perms))
for perm in perms:
  print("".join(perm))
