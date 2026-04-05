import strategies
import engine

GRID_SIZE = 16

CROP_LAYOUT = [
	(3, "carrot"),
	(6, "pumpkin"),
	(9, "sunflower"),
	(13, "cactus"),
	(16, "hay")
]

CROP_ACTIONS = {
	"carrot": strategies.carrot,
	"pumpkin": strategies.pumpkin,
	"sunflower": strategies.sunflower,
	"cactus": strategies.cactus,
	"hay": strategies.hay,
}


def choose_crop(x):
	for limit, crop in CROP_LAYOUT:
		if x < limit:
			return crop
	return "hay"


def execute_crop(crop_type, x, y):
	if crop_type not in CROP_ACTIONS:
		strategies.hay(x, y)
		return

	action = CROP_ACTIONS[crop_type]
	action(x, y)


def process_tile(x, y):
	crop_type = choose_crop(x)
	execute_crop(crop_type, x, y)
	move(North)


def run():
	while True:
		engine.water_if_needed()

		for x in range(GRID_SIZE):
			for y in range(GRID_SIZE):
				process_tile(x, y)

			move(East)


run()