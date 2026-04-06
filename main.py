import strategies
import engine

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

def get_action(x, y):
	for limit, crop in CROP_LAYOUT:
		if x < limit:
			CROP_ACTIONS[crop](x, y)
			engine.water_if_needed()
			return

def run():
	change_hat(Hats.Green_Hat)
	while True:

		if num_items(Items.Bone) < 10000:
			engine.sweep_grid(strategies.clear_farm)
			strategies.grow_snake()
		else:
			engine.sweep_grid(get_action)

run()
