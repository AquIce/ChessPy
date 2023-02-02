moves = {
 'P': ((0, 1)),
 'T': ((-7, 0), (-6, 0), (-5, 0), (-4, 0), (-3, 0), (-2, 0), (-1, 0), (0, -7),
       (0, -6), (0, -5), (0, -4), (0, -3), (0, -2), (0, -1), (0, 0), (0, 1),
       (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 0), (2, 0), (3, 0),
       (4, 0), (5, 0), (6, 0), (7, 0)),
 'k': ((2, 1), (1, 2), (-2, 1), (1, -2), (2, -1), (-1, 2), (-2, -1), (-1, -2)),
 'B': ((-7, -7), (-7, 7), (-6, -6), (-6, 6), (-5, -5), (-5, 5), (-4, -4),
       (-4, 4), (-3, -3), (-3, 3), (-2, -2), (-2, 2), (-1, -1), (-1, 1),
       (0, 0), (1, -1), (1, 1), (2, -2), (2, 2), (3, -3), (3, 3), (4, -4),
       (4, 4), (5, -5), (5, 5), (6, -6), (6, 6), (7, -7), (7, 7)),
 'Q':
 ((-7, -7), (-7, 0), (-7, 7), (-6, -6), (-6, 0), (-6, 6), (-5, -5), (-5, 0),
  (-5, 5), (-4, -4), (-4, 0), (-4, 4), (-3, -3), (-3, 0), (-3, 3), (-2, -2),
  (-2, 0), (-2, 2), (-1, -1), (-1, 0), (-1, 1), (0, -7), (0, -6), (0, -5),
  (0, -4), (0, -3), (0, -2), (0, -1), (0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
  (0, 5), (0, 6), (0, 7), (1, -1), (1, 0), (1, 1), (2, -2), (2, 0), (2, 2),
  (3, -3), (3, 0), (3, 3), (4, -4), (4, 0), (4, 4), (5, -5), (5, 0), (5, 5),
  (6, -6), (6, 0), (6, 6), (7, -7), (7, 0), (7, 7)),
 'K':
 ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1))
}

moves = {
 'P': ((0, 1)),
 'T':
 tuple([(i, j) for i in range(-7, 8) for j in range(-7, 8) if i * j == 0]),
 'k':
 [(x, y) for x in [-2, -1, 1, 2] for y in [-2, -1, 1, 2] if (x, y) != (0, 0)],
 'B':
 tuple([(i, j) for i in range(-7, 8) for j in range(-7, 8)
        if abs(i) == abs(j)]),
 'Q':
 tuple([(i, j) for i in range(-7, 8) for j in range(-7, 8)
        if i * j == 0 or abs(i) == abs(j)]),
 'K':
 tuple([(i, j) for i in range(-1, 2) for j in range(-1, 2)])
}

print(moves['T'])


game_grid = [['  ', '  ', '  ', '  ', '  ', '  ', '  ', ' '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']]
game_grid = [[' '] * 8] * 8