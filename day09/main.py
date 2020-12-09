def check_is_sum(number, cache):
    for option in cache:
        part = number - option
        if part in cache and part != option:
            return True
    return False


def solve1():
    cache = []
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.rstrip()
            number = int(line)
            if len(cache) == 25:
                if not check_is_sum(number, cache):
                    return number
                else:
                    cache = cache[1:]
            cache.append(number)
    return -1


def solve2():
    weakness = solve1()
    contiguous = []
    all_numbers = []
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.rstrip()
            number = int(line)
            all_numbers.append(number)
    for number in all_numbers:
        contiguous.append(number)
        if sum(contiguous) == weakness:
            return min(contiguous) + max(contiguous)
        while sum(contiguous) > weakness:
            del contiguous[0]
            if sum(contiguous) == weakness:
                return min(contiguous) + max(contiguous)


if __name__ == '__main__':
    print(solve1())
    print(solve2())
