import engine

GRID_SIZE = 16
tile_counters = {}

def clear_farm(x, y):
	if can_harvest():
		harvest()

def get_tile_key(x, y):
	return (x, y)

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
	if get_ground_type() == Grounds.Soil:
		till()
	if get_entity_type() != Entities.Tree:
		plant(Entities.Tree)
		return
	if can_harvest():
		harvest()
		plant(Entities.Tree)

def pumpkin(x, y):
	key = get_tile_key(x, y)
	if key not in tile_counters:
		tile_counters[key] = 0
	
	fase = tile_counters[key]
	entidade = get_entity_type()

	if fase == 0:
		if entidade != Entities.Pumpkin:
			engine.prepare_tile()
			plant(Entities.Pumpkin)
		tile_counters[key] = 1
		return
	elif fase == 1:
		if entidade != Entities.Pumpkin:
			engine.prepare_tile()
			plant(Entities.Pumpkin)
			tile_counters[key] = 1
		else:
			tile_counters[key] = 2
		return
	elif fase == 2:
		if entidade == Entities.Pumpkin:
			if can_harvest():
				harvest()
				engine.prepare_tile()
				plant(Entities.Pumpkin)
				tile_counters[key] = 1
		else:
			tile_counters[key] = 0

def sunflower(x, y):
	if get_entity_type() != Entities.Sunflower:
		engine.prepare_tile()
		plant(Entities.Sunflower)
	elif can_harvest():
		if measure() >= 7:
			harvest()
			plant(Entities.Sunflower)

def hay(x, y):
	if get_ground_type() == Grounds.Soil:
		till()
	if can_harvest():
		harvest()
	plant(Entities.Grass)

def cactus(x, y):
	if get_entity_type() != Entities.Cactus:
		engine.prepare_tile()
		plant(Entities.Cactus)
		return
	
	current = measure()
	if x < GRID_SIZE - 1:
		east = measure(East)
		if east != None and current > east:
			swap(East)
	if y < GRID_SIZE - 1:
		north = measure(North)
		if north != None and current > north:
			swap(North)
	if can_harvest():
		harvest()

def grow_snake():
	if measure() == None:
		change_hat(Hats.Carrot_Hat) 
		return

	change_hat(Hats.Dinosaur_Hat)
	while True:
		apple = measure()
		if apple == None:
			break
		
		if not move_safe(apple[0], apple[1]):
			break
			
	engine.move_to_origin()
	change_hat(Hats.Carrot_Hat) 

def move_safe(tx, ty):
	while get_pos_x() != tx or get_pos_y() != ty:
		moved = False
		
		if get_pos_x() < tx:
			if move(East):
				moved = True
		elif get_pos_x() > tx:
			if move(West):
				moved = True
			
		if not moved:
			if get_pos_y() < ty:
				if move(North):
					moved = True
			elif get_pos_y() > ty:
				if move(South):
					moved = True
				
	
		if not moved:
			for d in [North, East, South, West]:
				if move(d):
					moved = True
					break
			if not moved:
				return False
	return True
