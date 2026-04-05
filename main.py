import strategies
import engine

GRID_SIZE = 16
CROP_LAYOUT = [
	(2, "carrot"),
	(5, "pumpkin"),
	(8, "sunflower"),
	(12, "cactus"),
	(14, "hay"),
	(16, "tree")
]
CROP_ACTIONS = {
	"carrot": strategies.carrot,
	"pumpkin": strategies.pumpkin,
	"sunflower": strategies.sunflower,
	"cactus": strategies.cactus,
	"hay": strategies.hay,
	"tree": strategies.tree
}

def choose_crop(x):
	for limit, crop in CROP_LAYOUT:
		if x < limit:
			return crop
	return "hay"

def work_tile(x, y):
	crop_type = choose_crop(x)
	if crop_type in CROP_ACTIONS:
		action_func = CROP_ACTIONS[crop_type]
		action_func(x, y)
	else:
		strategies.hay(x, y)
	engine.water_if_needed()

def run():
	while True:
		if num_items(Items.Bone) < 10000:
			strategies.grow_snake()
		engine.sweep_grid(work_tile)

run()
