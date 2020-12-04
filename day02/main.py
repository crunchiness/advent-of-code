import re
from collections import Counter


def solve1():
    valid_count = 0
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            match = re.match('([0-9]{1,2})-([0-9]{1,2}) ([a-z]): ([a-z]+)', line)
            min_ = int(match.group(1))
            max_ = int(match.group(2))
            letter = match.group(3)
            password = match.group(4)
            letter_count = Counter(password).get(letter)
            if letter_count is not None:
                valid_count += min_ <= letter_count <= max_
    print(valid_count)


def solve2():
    valid_count = 0
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            match = re.match('([0-9]{1,2})-([0-9]{1,2}) ([a-z]): ([a-z]+)', line)
            index1_ = int(match.group(1))
            index2_ = int(match.group(2))
            letter = match.group(3)
            password = match.group(4)
            if (password[index1_ - 1] == letter) ^ (password[index2_ - 1] == letter):
                valid_count += 1
    print(valid_count)


if __name__ == '__main__':
    solve1()
    solve2()
