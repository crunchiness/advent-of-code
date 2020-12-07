def parse_boarding_pass(bp: str):
    row = int(bp[:7].replace('F', '0').replace('B', '1'), 2)
    col = int(bp[7:].replace('L', '0').replace('R', '1'), 2)
    seat_id = row * 8 + col
    return seat_id, row, col


def solve1():
    with open('input.txt', 'r') as f:
        return max([parse_boarding_pass(line.rstrip())[0] for line in f])


def solve2():
    with open('input.txt', 'r') as f:
        ids = [parse_boarding_pass(line.rstrip())[0] for line in f]
        sorted_ids = sorted(ids)
        previous = sorted_ids[0]
        for seat_id in sorted_ids[1:]:
            if seat_id == previous + 2:
                return previous + 1
            else:
                previous = seat_id


if __name__ == '__main__':
    print(solve1())
    print(solve2())
