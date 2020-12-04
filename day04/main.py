import re
from typing import List

req = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
req_count = len(req)


def solve1():
    valid_count = 0
    with open('input.txt', 'r') as f:
        has_req_count = 0
        for line in f.readlines() + ['\n']:
            if line == '\n':
                if has_req_count >= req_count:
                    valid_count += 1
                has_req_count = 0
            else:
                for attr in line.split(' '):
                    if attr.split(':')[0] in req:
                        has_req_count += 1
    print(valid_count)


class PassportValidation:
    def __init__(self):
        self.byr = False
        self.iyr = False
        self.eyr = False
        self.hgt = False
        self.hcl = False
        self.ecl = False
        self.pid = False

    def is_valid(self):
        return self.byr and self.iyr and self.eyr and self.hgt and self.hcl and self.ecl and self.pid

    def add_fields(self, fields: List[str]):
        for field in fields:
            k = field[:3]
            v = field[4:]
            try:
                if k == 'byr':
                    if 1920 <= int(v) <= 2002:
                        self.byr = True
                elif k == 'iyr':
                    if 2010 <= int(v) <= 2020:
                        self.iyr = True
                elif k == 'eyr':
                    if 2020 <= int(v) <= 2030:
                        self.eyr = True
                elif k == 'hgt':
                    unit = v[-2:]
                    value = int(v[:-2])
                    if unit == 'cm' and 150 <= value <= 193:
                        self.hgt = True
                    elif unit == 'in' and 59 <= value <= 76:
                        self.hgt = True
                elif k == 'hcl':
                    if re.match('#[0-9a-f]{6}$', v) is not None:
                        self.hcl = True
                elif k == 'ecl':
                    if v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                        self.ecl = True
                elif k == 'pid':
                    if re.match('[0-9]{9}$', v) is not None:
                        self.pid = True
            except ValueError:
                pass


def solve2():
    valid_count = 0
    with open('input.txt', 'r') as f:
        pv = PassportValidation()
        for line in f.readlines() + ['\n']:
            if line == '\n':
                if pv.is_valid():
                    valid_count += 1
                pv = PassportValidation()
            else:
                pv.add_fields(line.rstrip().split(' '))
    print(valid_count)


if __name__ == '__main__':
    solve1()
    solve2()
