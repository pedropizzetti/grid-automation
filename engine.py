def harvest_if_ready():
	if can_harvest():
		harvest()


def ensure_tilled():
	if get_ground_type() == Grounds.Grassland:
		till()


def prepare_tile_for_planting():
	if can_harvest():
		harvest()
	
	if get_ground_type() == Grounds.Grassland:
		till()


def plant_crop(crop):
	prepare_tile_for_planting()
	plant(crop)
	
WATER_THRESHOLD = 0.40
def water_if_needed():
	if get_water() < WATER_THRESHOLD:
		use_item(Items.Water)