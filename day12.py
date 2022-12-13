from collections import deque

with open('input_day12.txt') as f:
  lines = f.read().strip().splitlines()

#y means rows, x means columns in this case, G stands for grid, c stands for character
G = []
start, end = None, None
for y, line in enumerate(lines):
  G.append([])
  for x, c in enumerate(line):
    if c == 'S':
      start = x, y
      c = 'a'
    elif c == 'E':
      end = x, y
      c = 'z'
    G[y].append(ord(c))

# G[y].append(ord(c)) fills the row with the ordinal 
# equivalent of the characters
# pos stands for position (will be using the starting position 'S' from the previous search), 
# q stands for queue
# d stands for distance, nx stands for node x and ny for node y
# while q means it will loop forever
# deque is just so we can use popleft() and being more efficient with resources

def BFS(G, pos):
  q = deque([(pos, 0)])
  seen = set([pos])
  #print(q, seen)
  while q:
    (x, y), d = q.popleft()
    if (x, y) == end:
      return d
    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
      nx, ny = x + dx, y + dy
      if (nx, ny) in seen:
        continue
      if 0 <= nx < len(G[0]) and 0 <= ny < len(G):
        if G[ny][nx] > G[y][x] + 1:
          continue
        seen.add((nx, ny))
        q.append(((nx, ny), d + 1))

print(BFS(G, start))