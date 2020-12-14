import re
from itertools import product


def is_mask(line):
    return line[:4] == 'mask'


def parse_mask(line):
    return line[7:]


def parse_mem(line):
    match = re.match('^mem\[([0-9]+)\] = ([0-9]+)$', line)
    return int(match.group(1)), int(match.group(2))


def apply_mask(mask, value):
    ones_mask = int(''.join(['1' if bit == '1' else '0' for i, bit in enumerate(mask)]), 2)
    zeros_mask = int(''.join(['0' if bit == '0' else '1' for i, bit in enumerate(mask)]), 2)
    value |= ones_mask
    value &= zeros_mask
    return value


def solve1():
    mask = None
    mem_dict = {}
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.rstrip()
            if is_mask(line):
                mask = parse_mask(line)
            else:
                index, value = parse_mem(line)
                value = apply_mask(mask, value)
                mem_dict[index] = value
    return sum(mem_dict.values())


def address_gen(mask, index):
    index_str = bin(index)[2:].zfill(36)
    template = ''.join((m if m in '1X' else b for b, m in zip(index_str, mask)))
    for combination in product('01', repeat=template.count('X')):
        address = ''
        x_index = 0
        for i, b in enumerate(template):
            if b == 'X':
                address += combination[x_index]
                x_index += 1
            else:
                address += b
        yield address


def solve2():
    mask = None
    mem_dict = {}
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.rstrip()
            if is_mask(line):
                mask = parse_mask(line)
            else:
                index, value = parse_mem(line)
                for address in address_gen(mask, index):
                    mem_dict[int(address)] = value
    return sum(mem_dict.values())


if __name__ == '__main__':
    print(solve1())
    print(solve2())
