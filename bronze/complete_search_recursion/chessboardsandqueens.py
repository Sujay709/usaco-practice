from itertools import permutations

board = []
for _ in range(8):
  board.append(input())

valid_boards = 0

for rows in permutations(range(8)):
  is_safe = True
  for c in range(8):
    r = rows[c]
    if board[r][c] == "*":
      is_safe = False
      break
  if not is_safe:
    continue
  diag1_taken = [False] * 15
  for c in range(8):
    r = rows[c]
    diag_sum = r +c

    if diag1_taken[diag_sum]:
      is_safe = False
      break
    diag1_taken[diag_sum] = True
  if not is_safe:
    continue

  diag2_taken = [False] * 15
  for c in range(8):
    r = rows[c]
    diag_diff = r - c +7
    if diag2_taken[diag_diff]:
      is_safe = False
      break
    diag2_taken[diag_diff] = True
  if is_safe:
    valid_boards += 1

print(valid_boards)