class Tile:
	def __init__(self, tile_id, pixels, m, n):
		self.tile_id = tile_id
		self.pixels = pixels
		self.m = m
		self.n = n
		self.parse_edges()
	
	def parse_edges(self):
		pass

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

from math import sqrt
def solve_tiles(filename):
	tiles = parse_tiles(filename)
	all_tiles = list(tiles.keys())
	grid_size = int(sqrt(len(all_tiles)))
	assert len(all_tiles) % grid_size == 0
	print(len(tiles))


solve_tiles('20.1.txt')
solve_tiles('20.txt')


