import re


def parse_program():
    program = []
    with open('input.txt', 'r') as f:
        for line in f:
            match = re.match('(acc|jmp|nop) ([+-][0-9]+)', line)
            program.append((match.group(1), int(match.group(2))))
    return program


def check_loop(program):
    acc = 0
    i = 0
    previous_i = -1
    executed_lines = []
    while True:
        if i in executed_lines:
            # is loop
            return previous_i, acc
        elif i == len(program):
            # program is OK
            return None, acc
        elif i > len(program):
            # program goes out of bounds
            return None, None
        else:
            executed_lines.append(i)

        previous_i = i
        instruction, value = program[i]
        if instruction == 'nop':
            i += 1
        elif instruction == 'acc':
            acc += value
            i += 1
        elif instruction == 'jmp':
            i += value


def solve1():
    program = parse_program()
    r, acc = check_loop(program)
    if r is not None and acc is not None:
        return acc


def solve2():
    program = parse_program()
    for i, (instruction, value) in enumerate(program):
        if instruction == 'jmp':
            r, acc = check_loop(program[:i] + [('nop', value)] + program[i+1:])
            if r is None and acc is not None:
                return acc
        if instruction == 'nop':
            r, acc = check_loop(program[:i] + [('jmp', value)] + program[i+1:])
            if r is None and acc is not None:
                return acc


if __name__ == '__main__':
    print(solve1())
    print(solve2())
