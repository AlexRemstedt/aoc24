import sys


def difference(report: list[int]) -> bool:
    for i, j in zip(report[:-1], report[1:]):
        diff = abs(i - j)
        if diff < 1 or diff > 3:
            return False
    return True


def inorder(report: list[int]) -> bool:
    return report[::-1] == sorted(report) or report == sorted(report)


input = [[int(num) for num in line.strip().split()] for line in sys.stdin]

always_good = sum(1 for report in input if inorder(
    report) and difference(report))

double_check = [
    report
    for report in input
    if not inorder(report) or inorder(report) and not difference(report)
]


def dampener(report: list[int]) -> bool:
    for i in range(len(report)):
        temp_rep = report[:i] + report[i + 1:]
        if not inorder(temp_rep):
            continue
        if not difference(temp_rep):
            continue
        return True
    return False


print(always_good + sum(1 for r in double_check if dampener(r)))
