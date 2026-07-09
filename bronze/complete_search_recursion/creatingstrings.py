import itertools

n = input()
perms = set(itertools.permutations(n))
print(len(perms))
for perm in perms:
  print("".join(perm))