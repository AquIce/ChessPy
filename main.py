import os
import colorama as clr
import readchar

clr.init()
game_grid = [['  ' for _ in range(8)] for _ in range(8)]

coords = {
 'Pb': [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1]],
 'Rb': [[0, 0], [7, 0]],
 'Nb': [[1, 0], [6, 0]],
 'Bb': [[2, 0], [5, 0]],
 'Qb': [[3, 0]],
 'Kb': [[4, 0]],
 'Pw': [[0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6], [7, 6]],
 'Rw': [[0, 7], [7, 7]],
 'Nw': [[1, 7], [6, 7]],
 'Bw': [[2, 7], [5, 7]],
 'Qw': [[3, 7]],
 'Kw': [[4, 7]]
}

moves = {
 'P': ((0, 1), ),
 'R':
 tuple([(i, j) for i in range(-7, 8) for j in range(-7, 8)
        if i * j == 0 and (i, j) != (0, 0)]),
 'N':
 tuple([(i, j) for i in [-2, -1, 1, 2] for j in [-2, -1, 1, 2]
        if abs(i) != abs(j)]),
 'B':
 tuple([(i, j) for i in range(-7, 8) for j in range(-7, 8)
        if abs(i) == abs(j) and (i, j) != (0, 0)]),
 'Q':
 tuple([(i, j) for i in range(-7, 8) for j in range(-7, 8)
        if (i * j == 0 or abs(i) == abs(j)) and (i, j) != (0, 0)]),
 'K':
 tuple([(i, j) for i in range(-1, 2) for j in range(-1, 2)
        if (i, j) != (0, 0)])
}

winner = None

last_move = {'start': [], 'end': []}


def place_pieces():
	global game_grid
	game_grid = [['  ' for _ in range(8)] for _ in range(8)]
	for i in coords.keys():
		for j in coords[i]:
			if j != [-1, -1]:
				game_grid[j[1]][j[0]] = i

def format_grid_piece(piece):
	if piece[1] == 'w':
		return piece[0].upper()
	return piece[0].lower()

def output_grid():
	white = True
	place_pieces()
	for i in range(len(game_grid)):
		for j in range(len(game_grid[i])):
			if j == 0:
				print(8 - i, end=' ')
			if not white:
				print(clr.Back.BLACK + clr.Fore.WHITE + f' {format_grid_piece(game_grid[i][j])} ' +
				      clr.Fore.RESET + clr.Back.RESET,
				      end='')
			else:
				print(clr.Back.WHITE + clr.Fore.BLACK + f' {format_grid_piece(game_grid[i][j])} ' +
				      clr.Fore.RESET + clr.Back.RESET,
				      end='')
			if j != 7:
				white = not white
		print()

	print('   a  b  c  d  e  f  g  h')


def is_occuped(coords_to_check):
	for i in list(coords.values()):
		if coords_to_check in i:
			return True
	return False


def get_free_points():
	frp = []
	for i in range(8):
		for j in range(8):
			if not is_occuped([i, j]):
				frp.append([i, j])
	return frp


def eliminate(coos):
	result = [(i, j) for i in coords.keys() for j in range(len(coords[i]))
	          if coords[i][j] == coos]
	coords[result[0][0]][result[0][1]] = [-1, -1]


def find_path(start, end):
	path = []
	if start[0] == end[0]:
		if start[1] > end[1]:
			path = [[start[0], start[1] + i - 1]
			        for i in range(0, end[1] - start[1], -1)]
		else:
			path = [[start[0], start[1] + i + 1] for i in range(end[1] - start[1])]
	elif start[1] == end[1]:
		if start[0] > end[0]:
			path = [[start[0] + i - 1, start[1]]
			        for i in range(0, end[0] - start[0], -1)]
		else:
			path = [[start[0] + i + 1, start[1]] for i in range(end[0] - start[0])]
	else:
		if start[0] < end[0] and start[1] < end[1]:
			path = [[
			 i, j
			] for i, j in zip([start[0] + i + 1 for i in range(end[0] - start[0])],
			                  [start[1] + i + 1 for i in range(end[1] - start[1])])]
		elif start[0] > end[0] and start[1] < end[1]:
			path = [[i, j] for i, j in
			        zip([start[0] + i - 1 for i in range(0, end[0] - start[0], -1)],
			            [start[1] + i + 1 for i in range(end[1] - start[1])])]
		elif start[0] < end[0] and start[1] > end[1]:
			path = [[
			 i, j
			] for i, j in zip([start[0] + i + 1 for i in range(
			 end[0] -
			 start[0])], [start[1] + i - 1 for i in range(0, end[1] - start[1], -1)])]
		else:
			path = [[i, j] for i, j in
			        zip([start[0] + i - 1 for i in range(0, end[0] - start[0], -1)],
			            [start[1] + i - 1 for i in range(0, end[1] - start[1], -1)])]
	return path


def check_collisions(start, end, piece):
	elim_piece = None
	if piece[0] == 'P':
		...
	elif piece[0] == 'N':
		if end not in get_free_points():
			try:
				end_key = [k for k, v in coords.items() if end in v][0]
			except:
				return False, None
			if piece[1] != end_key[1]:
				return True, end_key
			return False, None
		return True, None

	for i in find_path(start, end):
		if not i in get_free_points():
			try:
				end_key = [k for k, v in coords.items() if end in v][0]
			except:
				return False, None
			elim_piece = end_key
			if not (i == end and piece[1] != end_key[1]):
				if piece[0] == 'k' and piece[1] != end_key[1]:
					return True, end_key
				return False, None
	return True, elim_piece


def get_point_color(point):
	p_color = [k for k, v in coords.items() if point in v]
	if p_color == []: return ''
	return [k for k, v in coords.items() if point in v][0][1]


def get_point_piece(point, strmode=False):
	for i in coords:
		for j in range(len(i)):
			if i[j] == point:
				return i, j
	if not strmode: return []
	return ''


def get_possible_moves(piece, index=0):
	el = False
	to_rem_pawn = []
	without_collisions = []
	co = coords[piece][index]
	# print(f'Coordinates : {co}\n')
	if piece == 'Pw':
		if is_occuped([co[0], co[1] - 1]):
			to_rem_pawn = [co[0], co[1] - 1]
		if co[1] == 6:
			moves['P'] = ((0, -1), (0, -2))
			# without_collisions.extend([co[0] - 2, co[1]])
		else:
			moves['P'] = ((0, -1), )

		ext = [[co[0] + i, co[1] - 1] for i in [1, -1] if [co[0] + i, co[1] - 1] not in get_free_points() and get_point_color([co[0] + i, co[1] - 1]) == 'b']
		
		if ext != []:
			el = True
			without_collisions.extend(ext)
			
	elif piece == 'Pb':
		if is_occuped([co[0], co[1] + 1]):
			to_rem_pawn = [co[0], co[1] + 1]
		if co[1] == 1:
			moves['P'] = ((0, 1), (0, 2))
			
		ext = [[co[0] + i, co[1] + 1] for i in [1, -1] if [co[0] + i, co[1] + 1] not in get_free_points() and get_point_color([co[0] + i, co[1] + 1]) == 'w']
		
		if ext != []:
			el = True
			without_collisions.extend(ext)
			
	without_collisions.extend([[co[0] + i, co[1] + j] for (i, j) in moves[piece[0]] if co[0] + i >= 0 and co[0] + i < 8 and co[1] + j >= 0 and co[1] + j < 8])

	if to_rem_pawn != []:
		without_collisions.remove(to_rem_pawn)
		to_rem_pawn = []
	moves['P'] = ((0, 1), )
	# print(f'Without collisions : {without_collisions}\n')
	ok = [i for i in without_collisions if check_collisions(co, i, piece)[0]]
	# print(f'Final moves : {ok}')
	return ok


def move(piece, coos: list, index=0):
	if coos not in get_free_points():
		eliminate(coos)
	coords[piece][index] = coos
	# print(coords)


def player_move(color):
	movs = []
	for piece in coords.keys():
		if piece[1] == color:
			for f_coords in range(len(coords[piece])):
				if coords[piece][f_coords] != [-1, -1]:
					if get_possible_moves(piece, f_coords) != []:
						for i in get_possible_moves(piece, f_coords):
							movs.append(((piece, f_coords), i))

	tmp_moves = [i[1] for i in movs]
	takes = [True if is_occuped(i) else False for i in tmp_moves]
	tmp_pieces = [i[0][0][0] for i in movs]
	for i in range(len(tmp_pieces)):
		if tmp_pieces[i].startswith('P'):
			tmp_alpha = 'abcdefgh'
			tmp_pieces[i] = tmp_alpha[movs[tmp_pieces[i]][0][0][0]] + tmp_pieces[i].replace('P', '') if takes[i] else tmp_pieces[i].replace('P', '')
	choice = selector_menu(tmp_moves, format_coords, tmp_pieces)

	global last_move
	'''print('move', movs[choice][1])
	print('f_coords', movs[choice][0][1])
	print('piece', movs[choice][0][0])'''
	last_move = []

	move(movs[choice][0][0], movs[choice][1], movs[choice][0][1])


def selector_menu(opts, format_fn=lambda x, y: x, start_pieces=[]):
	index = 0
	while True:
		os.system('clear')
		output_grid()

		options = [
		 f'\t{clr.Fore.GREEN}{format_fn(opts[i], start_pieces[i])}{clr.Style.RESET_ALL}'
		 for i in range(len(opts))
		]

		for i in range(len(options)):
			if i == index:
				print(f"{clr.Back.BLUE}", end="")
			print(options[i])

		ch = readchar.readkey()
		if ch == readchar.key.DOWN:
			index += 1
			if index == len(options):
				index = 0
		elif ch == readchar.key.UP:
			index -= 1
			if index == -1:
				index = len(options) - 1
		elif ch == readchar.key.ENTER:
			return index
		os.system('clear')


def format_coords(coords_to_format, start_piece=''):
	lt = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
	return f'{start_piece}{lt[coords_to_format[0]]}{8 - coords_to_format[1]}'


def main_loop():
	os.system('cls')
	while winner == None:
		os.system('clear')
		output_grid()
		player_move('w')
		os.system('clear')
		output_grid()
		player_move('b')


main_loop()
'''for i in range(8):
	eliminate([i, 6])
output_grid()
get_possible_moves('Pb', 4)
player_move('w')
get_possible_moves('Qw')
move('Qw', [3, 2])
output_grid()
get_possible_moves('Qw')
'''
