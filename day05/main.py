"""Day 5: Hydrothermal Venture"""

from collections import defaultdict

def get_horizontal_coords(x1, x2, y):
    return [(i, y) for i in range(min(x1, x2), max(x1, x2) + 1)]

def get_vertical_coords(y1, y2, x):
    return [(x, i) for i in range(min(y1, y2), max(y1, y2) + 1)]

def get_diagonal_coords(x1, y1, x2, y2):
    lx, ly, rx, ry = (x1, y1, x2, y2) if x1 <= x2 else (x2, y2, x1, y1)
    slope = 1 if ly <= ry else -1
    return [(lx + i, ly + i * slope) for i in range(rx - lx + 1)]

def build_plan(lines, include_diagonals=False):
    plan = defaultdict(int)

    for x1, y1, x2, y2 in lines:
        if y1 == y2:
            for point in get_horizontal_coords(x1, x2, y1):
                plan[point] += 1
        elif x1 == x2:
            for point in get_vertical_coords(y1, y2, x1):
                plan[point] += 1
        elif include_diagonals:
            for point in get_diagonal_coords(x1, y1, x2, y2):
                plan[point] += 1

    return plan

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [[int(n) for n in [*p1.split(','), *p2.split(',')]]
                 for p1, p2 in [l.strip().split(' -> ') for l in f.readlines()]]

    print('part 1:', sum([v > 1 for v in build_plan(lines).values()]))
    print('part 2:', sum([v > 1 for v in build_plan(lines, True).values()]))

