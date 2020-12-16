import math
import re


def parse_field(line):
    match = re.match('([ a-z]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)', line)
    field_name = match.group(1)
    range_lower = (int(match.group(2)), int(match.group(3)))
    range_upper = (int(match.group(4)), int(match.group(5)))
    return field_name, range_lower, range_upper


def is_value_valid(value, fields):
    for (x1, x2), (x3, x4) in fields.values():
        if x1 <= value <= x2 or x3 <= value <= x4:
            return True
    return False


def get_final_match(matches):
    for i, fields in matches.items():
        if len(fields) == 1:
            return i, fields[0]


def solve():
    fields = {}
    fields_finished = False
    nearby_tickets = []
    my_ticket = None

    # parsing input
    with open('input.txt', 'r') as f:
        while line := f.readline():
            line = line.rstrip()
            if line in ['', 'nearby tickets:']:
                continue
            elif line == 'your ticket:':
                fields_finished = True
                my_ticket = list(map(int, f.readline().split(',')))
            elif not fields_finished:
                field_name, range_lower, range_upper = parse_field(line)
                fields[field_name] = (range_lower, range_upper)
            else:
                nearby_tickets.append(list(map(int, line.split(','))))

    # prune tickets and calculate scanning error rate
    valid_nearby_tickets = []
    ser = 0
    for ticket in nearby_tickets:
        ticket_valid = True
        for value in ticket:
            if not is_value_valid(value, fields):
                ser += value
                ticket_valid = False
        if ticket_valid:
            valid_nearby_tickets.append(ticket)
    # part 1 answer
    print(ser)

    # by elimination, in the end there will be one true match
    matches = {i: list(fields.keys()) for i in range(len(my_ticket))}
    for ticket in valid_nearby_tickets:
        for i, value in enumerate(ticket):
            for field, ((x1, x2), (x3, x4)) in fields.items():
                if not (x1 <= value <= x2 or x3 <= value <= x4):
                    try:
                        matches[i].remove(field)
                    except ValueError:
                        pass

    # again by elimination we find other matches
    final_matches = {}
    while (match := get_final_match(matches)) is not None:
        i, field = match
        final_matches[i] = field
        for i in range(len(my_ticket)):
            try:
                matches[i].remove(field)
            except ValueError:
                pass

    # multiply departure fields
    # part 2 answer
    print(math.prod([my_ticket[i] if field.startswith('departure') else 1 for i, field in final_matches.items()]))


if __name__ == '__main__':
    solve()
