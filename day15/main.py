def solve1(final_round=2020):
    f = open('input.txt', 'r')
    puzzle_input = f.read().rstrip()
    f.close()
    numbers = list(map(int, puzzle_input.split(',')))
    mem = {}
    for i, n in enumerate(numbers):
        mem[n] = [i]
    last = numbers[-1]
    round_ = len(numbers)

    while round_ < final_round:
        if len(mem[last]) == 1:
            last = 0
        else:
            last = mem[last][-1] - mem[last][-2]

        if last not in mem:
            mem[last] = [round_]
        else:
            mem[last].append(round_)
            if len(mem[last]) == 3:
                del mem[last][0]
        round_ += 1
    return last


def solve2():
    return solve1(final_round=30000000)


if __name__ == '__main__':
    print(solve1())
    print(solve2())
