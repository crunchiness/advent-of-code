import re
from math import prod


def pop_at_depth(lst, depth):
    for _ in range(depth):
        lst = lst[-1]
    return lst.pop()


def append_at_depth(lst, depth, x):
    for _ in range(depth):
        lst = lst[-1]
    # merge digits
    if len(lst) > 0 and type(x) == int and type(lst[-1]) == int:
        x = int(str(lst[-1]) + str(x))
        lst.pop()
    lst.append(x)


def evaluate_flat(lst):
    total = lst[0]
    for i in range(1, len(lst), 2):
        if lst[i] == '*':
            total *= lst[i + 1]
        elif lst[i] == '+':
            total += lst[i + 1]
    return total


def evaluate_flat_addition_first(lst):
    # add parenthesis and recurse
    if '+' in lst and '*' in lst:
        return evaluate(re.sub(r'([0-9]+\+[0-9]+)', r'(\1)', ''.join(map(str, lst))), addition_first=True)
    elif '+' in lst:
        return sum(filter(lambda x: x != '+', lst))
    elif '*' in lst:
        return prod(filter(lambda x: x != '*', lst))
    return lst[0]


def evaluate(line, addition_first=False):
    eval_flat = evaluate_flat_addition_first if addition_first else evaluate_flat
    expression = []
    depth = 0
    for symbol in line:
        if symbol == ' ':
            continue
        elif symbol == '(':
            append_at_depth(expression, depth, [])
            depth += 1
        elif symbol == ')':
            depth -= 1
            res = eval_flat(pop_at_depth(expression, depth))
            append_at_depth(expression, depth, res)
        elif symbol in '+*':
            append_at_depth(expression, depth, symbol)
        else:
            append_at_depth(expression, depth, int(symbol))
    return eval_flat(expression)


def solve1():
    total = 0
    with open('input.txt', 'r') as f:
        for line in f:
            total += evaluate(line.rstrip())
    return total


def solve2():
    total = 0
    with open('input.txt', 'r') as f:
        for line in f:
            total += evaluate(line.rstrip(), addition_first=True)
    return total


if __name__ == '__main__':
    print(solve1())
    print(solve2())
