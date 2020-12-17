# Part 1
def count_active(pocket):
    active = 0
    for layer in pocket:
        for row in layer:
            for cube in row:
                if cube == '#':
                    active += 1
    return active


def new_cube(cube, active_neighbours):
    if cube == '#' and active_neighbours in [2, 3]:
        return '#'
    elif cube == '.' and active_neighbours == 3:
        return '#'
    return '.'


def count_active_neighbours(pocket, x, y, z):
    active_neighbours = 0
    for k in range(max(z - 1, 0), z + 2):
        for j in range(max(y - 1, 0), y + 2):
            for i in range(max(x - 1, 0), x + 2):
                if (i, j, k) == (x, y, z):
                    continue  # ignore self
                try:
                    active_neighbours += pocket[k][j][i] == '#'
                except IndexError:
                    continue
    return active_neighbours


def extend_pocket(pocket):
    layer_height = len(pocket[0]) + 2
    layer_width = len(pocket[0][0]) + 2

    for layer in pocket:
        for row in layer:
            row.insert(0, '.')
            row.append('.')
        layer.insert(0, ['.'] * layer_width)
        layer.append(['.'] * layer_width)
    pocket.insert(0, [['.'] * layer_width for _ in range(layer_height)])
    pocket.append([['.'] * layer_width for _ in range(layer_height)])


def apply_cycle(pocket):
    extend_pocket(pocket)
    new_pocket = [[[None] * len(pocket[0][0]) for _ in range(len(pocket[0]))] for _ in range(len(pocket))]
    for z, layer in enumerate(pocket):
        for y, row in enumerate(layer):
            for x, cube in enumerate(row):
                active_neighbours = count_active_neighbours(pocket, x, y, z)
                new_pocket[z][y][x] = new_cube(cube, active_neighbours)
    return new_pocket


def solve1():
    initial = []
    with open('input.txt', 'r') as f:
        for line in f:
            initial.append(list(line.rstrip()))
    pocket = [initial]
    for _ in range(6):
        pocket = apply_cycle(pocket)
    print(count_active(pocket))


# Part 2 - eh
def count_active4d(pocket):
    active = 0
    for space in pocket:
        for layer in space:
            for row in layer:
                for cube in row:
                    if cube == '#':
                        active += 1
    return active


def count_active_neighbours4d(pocket, x, y, z, zz):
    active_neighbours = 0
    for l in range(max(zz - 1, 0), zz + 2):
        for k in range(max(z - 1, 0), z + 2):
            for j in range(max(y - 1, 0), y + 2):
                for i in range(max(x - 1, 0), x + 2):
                    if (i, j, k, l) == (x, y, z, zz):
                        continue  # ignore self
                    try:
                        active_neighbours += pocket[l][k][j][i] == '#'
                    except IndexError:
                        continue
    return active_neighbours


def extend_pocket4d(pocket):
    space_height = len(pocket[0]) + 2
    layer_height = len(pocket[0][0]) + 2
    layer_width = len(pocket[0][0][0]) + 2

    for space in pocket:
        for layer in space:
            for row in layer:
                row.insert(0, '.')
                row.append('.')
            layer.insert(0, ['.'] * layer_width)
            layer.append(['.'] * layer_width)
        space.insert(0, [['.'] * layer_width for _ in range(layer_height)])
        space.append([['.'] * layer_width for _ in range(layer_height)])
    pocket.insert(0, [[['.'] * layer_width for _ in range(layer_height)] for _ in range(space_height)])
    pocket.append([[['.'] * layer_width for _ in range(layer_height)] for _ in range(space_height)])


def apply_cycle4d(pocket):
    extend_pocket4d(pocket)
    new_pocket = [
        [
            [
                [None] * len(pocket[0][0][0]) for _ in range(len(pocket[0][0]))
            ] for _ in range(len(pocket[0]))
        ] for _ in range(len(pocket))
    ]
    for zz, space in enumerate(pocket):
        for z, layer in enumerate(space):
            for y, row in enumerate(layer):
                for x, cube in enumerate(row):
                    active_neighbours = count_active_neighbours4d(pocket, x, y, z, zz)
                    new_pocket[zz][z][y][x] = new_cube(cube, active_neighbours)
    return new_pocket


def solve2():
    initial = []
    with open('input.txt', 'r') as f:
        for line in f:
            initial.append(list(line.rstrip()))
    pocket = [[initial]]
    for _ in range(6):
        pocket = apply_cycle4d(pocket)
    print(count_active4d(pocket))


if __name__ == '__main__':
    solve1()
    solve2()
