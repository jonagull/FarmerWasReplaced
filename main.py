
import h
top_pos = 21


change_hat(Hats.Sunflower_Hat)

plantingOrder = [
	Entities.Grass,
	Entities.Grass,
	Entities.Grass,
	Entities.Carrot,
	Entities.Carrot,
	Entities.Carrot,
	Entities.Carrot,
	Entities.Carrot,
	Entities.Cactus,
	Entities.Sunflower,
	Entities.Sunflower,
	Entities.Sunflower,
	Entities.Tree,
	Entities.Tree,
	Entities.Tree,
]

def handlePlanting(entity):
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

while True:
	entity = Entities.Pumpkin

	if (get_pos_x() < len(plantingOrder)):
		entity = plantingOrder[get_pos_x()]

	handlePlanting(entity)
	move(North)

	if get_pos_y() == top_pos:
		move(East)
		#h.moveToNext()


	
				
	
		
		
		