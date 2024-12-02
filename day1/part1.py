import sys

input = [line.strip().split() for line in sys.stdin]
left = []
right = []

for line in input:
    left.append(int(line[0]))
    right.append(int(line[-1]))

left.sort()
right.sort()

distances = sum(abs(l - r) for l, r in zip(left, right))

print(distances)
