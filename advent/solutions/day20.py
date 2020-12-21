class Tile:
	def __init__(self, tile_id, pixels, m):
		self.tile_id = tile_id
		self.pixels = pixels
		self.m = m
		self.parse_edges()
	
	def parse_edges(self):
		# (top, right, down, left)
		# ten spaces, read ltr or utd so t/b l/r match
		top_edge, bottom_edge, left_edge, right_edge = self.get_edges()
		top = self.get_edge(top_edge)
		right = self.get_edge(right_edge)
		down = self.get_edge(down_edge)
		left = self.get_edge(left_edge)

		reversed_top = ''.join(reversed(top))
		reversed_right = ''.join(reversed(right))
		reversed_down = ''.join(reversed(down))
		reversed_left = ''.join(reversed(left))

		"""
		     | 0       | 90       | 180       | 270
		------------------------------------------------
		hv   | urdl    | LuRd     | DLUR      | rDlU
		hV   | UlDr    | RULD     | dRuL      | ldru
		Hv   | dRuL    | ldru     | UlDr      | RULD
		HV   | DLUR    | rDlU     | urdl      | LuRd
		-------------------------------------------------
		"""

		def reverse_permutation(p):
			return (p[3], p[2], p[1], p[0])

		permutations = [
			(top, right, down, left),
			(reversed_left, top, reversed_right, down),
			(reversed_down, reversed_left, reversed_top, reversed_right),
			(right, reversed_down, left, reversed_top),
		]
		permutations.append(reverse_permutation(permutations[3]))
		permutations.append(reverse_permutation(permutations[2]))
		permutations.append(reverse_permutation(permutations[1]))
		permutations.append(reverse_permutation(permutations[0]))
		self.permutations = permutations
		
	def get_edges(self):
		"top bottom left right"
		return (
			[(x, 0) for x in range(self.m)],
			[(x, self.m - 1) for x in range(self.m)],
			[(0, y) for y in range(self.m)],
			[(self.m - 1, y) for y in range(self.m)]
		)

	def get_edge(self, edge):
		return ''.join("#" if p in self.pixels else '.' for p in edge)

	def get_permutations(self)

	def does_edge_match(top=None, bottom=None, left=None, right=None):
		assert any([top, bottom, left, right])
		perms = self.get_permutations()


import re
tile_p = re.compile(r'Tile (?P<tile_id>\d*?):')

def make_tile(tile_lines):
	tile_id = tile_p.match(tile_lines[0]).group('tile_id')
	assert len(tile_id) > 0
	pixels = set()
	for y, tile_line in enumerate(tile_lines[1:]):
		for x, char in enumerate(tile_line):
			if char == '#':
				pixels.add((x, y))
	tile = Tile(tile_id, pixels, x, y)
	return tile

def parse_tiles(filename):
	tiles = dict()
	buf = []
	for line in open('advent/input_files/'+ filename):
		line = line.strip()
		if line == '':
			tile = make_tile(buf)
			tiles[tile.tile_id] = tile
			buf = []
		else:
			buf.append(line)
	tile = make_tile(buf)
	tiles[tile.tile_id] = tile
	return tiles


from collections import namedtuple, deque
GameState = namedtuple("GameState", ['board', 'unplaced_tiles'])
PlacedTile = namedtuple("PlacedTile", ['tile_id', 'configuration'])
def get_tile(gamestate, p):
	b = gamestate.board
	try:
		row = b[p[0]]
		return row[p[1]]
	except:
		return None

def next_placeable_position(gamestate, m):
	for y in range(0, m+1):
		for x in range(0, m+1):
			if get_tile(gamestate, (x, y)) is None:
				return (x, y)

from math import sqrt
def solve_tiles(filename):
	tiles = parse_tiles(filename)
	all_tiles = list(tiles.keys())
	grid_size = int(sqrt(len(all_tiles)))
	assert len(all_tiles) % grid_size == 0
	state_queue = deque([GameState([], list(all_tiles))])
	done = False
	while not Done:
		assert state_stack
		current_state = state_queue.popleft()



	
	


solve_tiles('20.1.txt')
solve_tiles('20.txt')


