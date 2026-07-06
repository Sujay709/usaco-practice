n = (input())
cross_pairs = 0
for a in range(len(n)):
  for b in range(a+1, len(n)):
    for c in range(b+1, len(n)):
      for d in range(c+1, len(n)):
        cross_pairs += n[a] == n[c] and n[b] == n[d]

print(cross_pairs)