chess = [input() for _ in range(8)]
print(sum([chess[y][x] == "F" for y in range(8) for x in range(8) if not (y + x) % 2 ]))