import re


def parse_piece(txt: str):
    if txt.endswith('.'):
        txt = txt[:-1]
    if txt.endswith('s'):
        txt = txt[:-1]
    txt = txt[:-4]
    if txt == 'no other':
        return None, 0
    match = re.match('([0-9]+) (.+)', txt)
    return match.group(2), int(match.group(1))


def parse_rule(rule_txt: str):
    bag, contents_txt = rule_txt.split(' bags contain ')
    return bag, [parse_piece(x) for x in contents_txt.split(', ')]


def make_rule_dict():
    rule_dict = {}
    with open('input.txt', 'r') as f:
        for line in f:
            bag, contents = parse_rule(line.rstrip())
            rule_dict[bag] = contents
    return rule_dict


def solve1():
    rule_dict = make_rule_dict()
    applicable = set()
    search = ['shiny gold']
    while len(search) > 0:
        key = search.pop()
        for k, v in rule_dict.items():
            if key in list(zip(*v))[0]:
                applicable.add((k, tuple(v)))
                search.append(k)
    return len(applicable)


def get_count(rule_dict, key):
    total = 1
    rule = rule_dict[key]
    for kind, count in rule:
        if count > 0:
            total += count * get_count(rule_dict, kind)
    return total


def solve2():
    rule_dict = make_rule_dict()
    return get_count(rule_dict, 'shiny gold') - 1


if __name__ == '__main__':
    print(solve1())
    print(solve2())
