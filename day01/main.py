def solve1():
    with open('input.txt', 'r') as f:
        numbers = [int(x) for x in f.readlines()]
        for number in numbers:
            other = 2020 - number
            if other in numbers:
                print(number * other)
                return


def solve2():
    with open('input.txt', 'r') as f:
        numbers = [int(x) for x in f.readlines()]
        for number in numbers:
            others = 2020 - number
            for number_ in numbers:
                other = others - number_
                if other in numbers:
                    print(number * number_ * other)
                    return


if __name__ == '__main__':
    solve1()
    solve2()
