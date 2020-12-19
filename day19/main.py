import re


def parse_rule(line):
    rule_idx, rule_txt = line.split(':')
    rule_idx = int(rule_idx)
    rule_txt = rule_txt.strip()
    if rule_txt[0] == '"':
        return rule_idx, rule_txt[1]
    rule = []
    for rule_part in rule_txt.split('|'):
        rule.append(list(map(int, rule_part.strip().split(' '))))
    return rule_idx, rule


def convert_to_regex(rules, rule):
    if type(rule) == str:
        return rule
    if len(rule) == 1:
        return ''.join([convert_to_regex(rules, rules[rule_part]) for rule_part in rule[0]])
    if len(rule) == 2:
        # part 2 exceptions
        if rule == [[42], [42, 8]]:
            return f'(?:{convert_to_regex(rules, [rule[0]])})+'
        # this pattern is not supported by regex in Python so I just expanded until answer stopped changing
        if rule == [[42, 31], [42, 11, 31]]:
            rule = [
                [42, 31],
                [42, 42, 31, 31],
                [42, 42, 42, 31, 31, 31],
                [42, 42, 42, 42, 31, 31, 31, 31]
            ]
        return f"(?:{'|'.join(map(lambda x: convert_to_regex(rules, [x]), rule))})"


def solve():
    rules = {}
    messages = []
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.rstrip()
            if line == '':
                continue
            if ':' in line:
                rule_idx, rule = parse_rule(line)
                rules[rule_idx] = rule
            else:
                messages.append(line)

    regex = f'^{convert_to_regex(rules, rules[0])}$'

    # count matches
    print(sum(1 if re.match(regex, msg) else 0 for msg in messages))

    # part 2
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    regex = f'^{convert_to_regex(rules, rules[0])}$'

    # count matches
    print(sum(1 if re.match(regex, msg) else 0 for msg in messages))


if __name__ == '__main__':
    solve()
