def solve1(right=3, down=1):
    trees = 0
    with open('input.txt', 'r') as f:
        forest = f.readlines()
        w = len(forest[0])
        h = len(forest)
        i = 0
        j = 0
        while j < h - down:
            i += right
            i %= w - 1
            j += down
            if forest[j][i] == '#':
                trees += 1
    return trees


def solve2():
    part1 = solve1(right=1, down=1)
    part2 = solve1(right=3, down=1)
    part3 = solve1(right=5, down=1)
    part4 = solve1(right=7, down=1)
    part5 = solve1(right=1, down=2)
    print(part1 * part2 * part3 * part4 * part5)


if __name__ == '__main__':
    print(solve1())
    solve2()
