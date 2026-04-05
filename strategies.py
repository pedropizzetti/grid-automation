import engine

GRID_SIZE = 16
PUMPKIN_GROWTH_TICKS = 3

tile_counters = {}
active_tiles = set()


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
		engine.prepare_tile_for_planting()
		plant(crop)
		mark_active(x, y)
		return False
	return True

def carrot(x, y):
	engine.plant_crop(Entities.Carrot)


def pumpkin(x, y):
	key = get_tile_key(x, y)

	if key not in tile_counters:
		tile_counters[key] = 0

	if not ensure_crop(Entities.Pumpkin,x,y):
		tile_counters[key] = 0
		return

	tile_counters[key] += 1

	if tile_counters[key] >= PUMPKIN_GROWTH_TICKS and can_harvest():
		harvest()
		tile_counters[key] = 0
		mark_active(x, y)


def sunflower(x, y):
	if not ensure_crop(Entities.Sunflower, x, y):
		return

	if not can_harvest():
		return

	if measure() >= 7:
		harvest()
		engine.plant_crop(Entities.Sunflower)
		mark_active(x, y)


def hay(x, y):
	if get_ground_type() == Grounds.Soil:
		till()

	if can_harvest():
		harvest()
		mark_active(x, y)



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