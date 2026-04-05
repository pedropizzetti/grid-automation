import engine
GRID_SIZE = 16
active_tiles = set()
tile_counters = {}

def get_tile_key(x, y):
	return (x, y)

def mark_active(x, y):
	active_tiles.add((x, y))

def mark_neighbors(x, y):
	mark_active(x, y)
	if x > 0:
		mark_active(x - 1, y)
	if x < GRID_SIZE - 1:
		mark_active(x + 1, y)
	if y > 0:
		mark_active(x, y - 1)
	if y < GRID_SIZE - 1:
		mark_active(x, y + 1)

def ensure_crop(crop, x, y):
	current = get_entity_type()
	if current != crop:
		engine.prepare_tile()
		plant(crop)
		mark_active(x, y)
		return False
	return True

def carrot(x, y):
	if get_entity_type() != Entities.Carrot:
		engine.prepare_tile()
		plant(Entities.Carrot)
		return
	if can_harvest():
		harvest()
		engine.prepare_tile()
		plant(Entities.Carrot)
		
def tree(x, y):
	if (x + y) % 2 != 0:
		return
	if get_entity_type() != Entities.Tree:
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Tree)
		return
	if can_harvest():
		harvest()
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Tree)

def pumpkin(x, y):
	global tile_counters
	key = get_tile_key(x, y)
	if key not in tile_counters:
		tile_counters[key] = 0

	count = tile_counters[key]

	if count == 0:
		if get_entity_type() != Entities.Pumpkin:
			engine.prepare_tile()
			plant(Entities.Pumpkin)
		tile_counters[key] = 1

	elif count == 1:
		if get_entity_type() != Entities.Pumpkin:
			engine.prepare_tile()
			plant(Entities.Pumpkin)
			tile_counters[key] = 0
		elif can_harvest():
			harvest()
			engine.prepare_tile()
			plant(Entities.Pumpkin)
			tile_counters[key] = 0
		else:
			tile_counters[key] = 2

	elif count == 2:
		if can_harvest():
			harvest()
		engine.prepare_tile()
		plant(Entities.Pumpkin)
		tile_counters[key] = 0
		mark_active(x, y)

def sunflower(x, y):
	if not ensure_crop(Entities.Sunflower, x, y):
		return
	if not can_harvest():
		return
	if measure() >= 7:
		harvest()
		engine.smart_plant(Entities.Sunflower)
		mark_active(x, y)

def hay(x, y):
	if get_ground_type() == Grounds.Soil:
		till()
	if can_harvest():
		harvest()
		mark_active(x, y)
	plant(Entities.Grass)

def cactus(x, y):
	if not ensure_crop(Entities.Cactus, x, y):
		return
	current = measure()
	swapped = False
	if x < GRID_SIZE - 1:
		east = measure(East)
		if east != None and current > east:
			swap(East)
			current = east
			swapped = True
			mark_neighbors(x, y)
	if y < GRID_SIZE - 1:
		north = measure(North)
		if north != None and current > north:
			swap(North)
			current = north
			swapped = True
			mark_neighbors(x, y)
	if swapped:
		return
	if not can_harvest():
		return
	if x < GRID_SIZE - 1:
		east = measure(East)
		if east == None or current > east:
			return
	if y < GRID_SIZE - 1:
		north = measure(North)
		if north == None or current > north:
			return
	harvest()
	mark_neighbors(x, y)

def grow_snake():
	change_hat(Hats.Dinosaur_Hat)
	while True:
		coords = measure()
		if coords == None:
			break
		ax = coords[0]
		ay = coords[1]
		success = move_to_apple(ax, ay)
		if not success:
			break
	while get_pos_y() > 0:
		move(South)
	while get_pos_x() > 0:
		move(West)
	change_hat(Hats.Green_Hat)

def move_to_apple(tx, ty):
	while get_pos_x() != tx or get_pos_y() != ty:
		if get_pos_x() != tx:
			if get_pos_x() < tx:
				if not move(East):
					return False
			else:
				if not move(West):
					return False
		if get_pos_y() != ty:
			if get_pos_y() < ty:
				if not move(North):
					return False
			else:
				if not move(South):
					return False
	return True
