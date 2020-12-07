def solve1():
    total = 0
    with open('input.txt', 'r') as f:
        yes_set = set()
        for line in f.readlines() + ['\n']:
            if line == '\n':
                total += len(yes_set)
                yes_set = set()
            else:
                yes_set.update(list(line.rstrip()))
    return total


def solve2():
    total = 0
    with open('input.txt', 'r') as f:
        yes_set = None
        for line in f.readlines() + ['\n']:
            if line == '\n':
                total += len(yes_set)
                yes_set = None
            elif yes_set is None:
                yes_set = set(list(line.rstrip()))
            else:
                yes_set.intersection_update(list(line.rstrip()))
    return total


if __name__ == '__main__':
    print(solve1())
    print(solve2())
