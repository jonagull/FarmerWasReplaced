

import h

change_hat(Hats.Sunflower_Hat)
top_pos = 21

grid = []
i = 0
while i < 22:
	row = []
	j = 0
	while j < 22:
		row.append(None)
		j += 1
	grid.append(row)
	i += 1
	

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

def getCompanion():
	x = get_pos_x()
	y = get_pos_y()
	return grid[y][x]

def handlePlanting(entity):
	companion = getCompanion()
	if companion != None:
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
	#print(compInfo)
	companion = compInfo[0]
	x = compInfo[1][0]
	y = compInfo[1][1]

	grid[y][x] = companion


while True:
	entity = Entities.Pumpkin

	if (get_pos_x() < len(plantingOrder)):
		entity = plantingOrder[get_pos_x()]

	companion = get_companion()
	if (companion != None):
		setCompanion(companion)

	handlePlanting(entity)
	move(North)

	if get_pos_y() == top_pos:
		move(East)
		#h.moveToNext()

