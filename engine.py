WATER_THRESHOLD = 0.45 

def move_to_origin():
	while get_pos_y() > 0:
		move(South)
	while get_pos_x() > 0:
		move(West)

def sweep_grid(action_func):
	size = 16
	for x in range(size):
		for y in range(size):
			action_func(x, y)
			

			if y < size - 1:
				move(North)
		
		for _ in range(size - 1):
			move(South)
			
		if x < size - 1:
			move(East)
			
	move_to_origin()


def prepare_tile():
	if can_harvest():
		harvest()
	
	if get_ground_type() == Grounds.Grassland:
		till()

def water_if_needed():
	if get_water() < WATER_THRESHOLD:
		use_item(Items.Water) 


def smart_plant(crop):
	prepare_tile()
	water_if_needed()
	plant(crop)

def prepare_for_pumpkin():
	if get_ground_type() == Grounds.Grassland:
		till()
	water_if_needed()

def plant_crop(crop):
	prepare_tile()
	plant(crop)

def ensure_tilled():
	if get_ground_type() == Grounds.Grassland:
		till()	
