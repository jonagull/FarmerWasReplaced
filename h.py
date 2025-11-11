def moveToNext():
	move(East)
	move(North)
	
def plantPumpkin():
	harvest()
	if (get_ground_type() == Grounds.Grassland):
		till()
	plant(Entities.Pumpkin)

	
def plantCarrot():
	harvest()
	if (get_ground_type() == Grounds.Grassland):
		till()
	plant(Entities.Carrot)
	
def plantBush():
	harvest()
	if (get_ground_type() == Grounds.Grassland):
		till()
	plant(Entities.Bush)
	
def plantTree():
	if can_harvest():
		harvest()
	plant(Entities.Tree)
	use_item(Items.Water)
	
def plantSunflower():
	if can_harvest():
		harvest()
	if (get_ground_type() == Grounds.Grassland):
		till()
	plant(Entities.Sunflower)
	
	
def plantGrass():
	if can_harvest():
		harvest()
	if (get_ground_type() == Grounds.Soil):
		till()
		
		
def plantCactus():
	if can_harvest():
		harvest()
	if (get_ground_type() == Grounds.Grassland):
		till()
	plant(Entities.Cactus)