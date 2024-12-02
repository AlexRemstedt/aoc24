import sys

input = [line.strip().split() for line in sys.stdin]
left, right = zip(*input)
left = list(map(int, left))
right = list(map(int, right))

hm = {}
for val in right:
    hm[val] = hm.get(val, 0) + 1

res = 0
for item in left:
    res += item * hm[item] if item in hm else 0

print(res)
