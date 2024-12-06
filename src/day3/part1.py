import re
import sys

input: list[str] = [str(line.strip()) for line in sys.stdin]
pat = r"mul\(\d+,\d+\)"
mul: list[str] = []
for s in input:
    mul += re.findall(pat, s)


def get_numbers(s: str) -> tuple[int, ...]:
    return tuple(map(int, iter(s[4:-1].split(","))))


nums = [get_numbers(s) for s in mul]

print(sum(d1 * d2 for d1, d2 in nums))
