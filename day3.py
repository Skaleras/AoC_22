import string
from itertools import zip_longest

letters = string.ascii_letters

with open('input_day3.txt', 'r') as f:
    lines = [l.strip('\n') for l in f.readlines()]

sum_ = 0

for w in lines:
    a, b = w[:len(w)//2], w[len(w)//2:]
    sum_ += letters.index([c for c in a if c in b][0]) + 1

print(sum_)

sum_2 = 0
groups = list(zip_longest(*[iter(lines)]*3, fillvalue=''))

for (a, b, c) in groups:
    sum_2 += letters.index([x for x in a if x in b and x in c][0]) + 1

print(sum_2)