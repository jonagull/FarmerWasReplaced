
import h

change_hat(Hats.Sunflower_Hat)
top_pos = 21

grid = [[None for _ in range(22)] for _ in range(22)]

plantingOrder = [
	Entities.Grass,
	Entities.Grass,
	Entities.Grass,
	Entities.Grass,
	Entities.Grass,
	Entities.Grass,
	Entities.Tree,
	Entities.Tree,
	Entities.Tree,
	Entities.Tree,
	Entities.Tree,
	Entities.Tree,
	Entities.Tree,
	Entities.Tree,
	Entities.Carrot,
	Entities.Cactus,
	Entities.Sunflower,
	Entities.Sunflower,
	Entities.Sunflower,
	Entities.Tree,
	Entities.Tree,
	Entities.Tree,
]

getCompanion():
    x = get_pos_x()
    y = get_pos_y()
    entity = grid[y][x]

def handlePlanting(entity):
    companion = getCompanion()
    
    if (companion is not None):
        entity = companion

	if entity == Entities.Grass:
		h.plantGrass()
	elif entity == Entities.Cactus:
		h.plantCactus()
	elif entity == Entities.Tree:
		h.plantTree()
	else:
		harvest()
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(entity)

def setCompanion(compInfo):
    companion = compInfo[0]
    x = compInfo[1]
    y = compInfo[2]

    grid[y][x] = companion


while True:
	entity = Entities.Pumpkin

	if (get_pos_x() < len(plantingOrder)):
		entity = plantingOrder[get_pos_x()]


	companion = get_companion()
    if (companion is not None):
        setCompanion(companion)

	handlePlanting(entity)
	move(North)

	if get_pos_y() == top_pos:
		move(East)
		#h.moveToNext()

