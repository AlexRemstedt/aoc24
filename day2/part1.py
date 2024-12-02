import sys

input = [[int(num) for num in line.strip().split()] for line in sys.stdin]


def is_decreasing(report: list[int]) -> bool:
    return report[::-1] == sorted(report)


def is_increasing(report: list[int]) -> bool:
    return report == sorted(report)


potentially_good = [
    report for report in input if is_increasing(report) or is_decreasing(report)
]


def difference(report: list[int]) -> bool:
    for i, j in zip(report[:-1], report[1:]):
        diff = abs(i - j)
        if diff < 1 or diff > 3:
            return False
    return True


print(sum(1 for r in potentially_good if difference(r)))
