from typing import List


def solve1():
    adapters = []
    with open('input.txt', 'r') as f:
        for line in f:
            adapters.append(int(line.rstrip()))
    diffs = []
    prev = 0
    for adapter in sorted(adapters):
        diffs.append(adapter - prev)
        prev = adapter
    diffs.append(3)
    ones = len(list(filter(lambda x: x == 1, diffs)))
    threes = len(list(filter(lambda x: x == 3, diffs)))
    return ones * threes


def count_streak(streak: List[int]):
    # Special case and I know that streak's length is 4
    if streak[0] == 1:
        return 7

    if len(streak) in [1, 2]:
        return 1
    if len(streak) == 3:
        return 2
    if len(streak) == 4:
        return 4
    if len(streak) == 5:
        return 7


def solve2():
    adapters = []
    with open('input.txt', 'r') as f:
        for line in f:
            adapters.append(int(line.rstrip()))
    streak = []
    prev = 0
    total = 1
    for adapter in sorted(adapters):
        if adapter - prev == 1:
            streak.append(adapter)
        else:
            total *= count_streak(streak)
            streak = [adapter]
        prev = adapter
    total *= count_streak(streak)
    return total


if __name__ == '__main__':
    print(solve1())
    print(solve2())
