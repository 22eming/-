R, C = map(int, input().split(' '))
result = []

puzzle_c = [input() for _ in range(R)]
puzzle_r = [ ''.join([puzzle_c[r][c] for r in range(R)]) for c in range(C) ]
puzzle = puzzle_c + puzzle_r

for p in puzzle:
    result.extend(p.split('#'))

for res in sorted(result):
    if len(res) >1:
        print(res)
        break