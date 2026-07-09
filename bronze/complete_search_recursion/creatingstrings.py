from itertools import permutations

n = input()
# Use set to filter out duplicate strings
perms = set(permutations(n))
print(len(perms))
for perm in perms:
  print("".join(perm))