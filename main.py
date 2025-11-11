import h
top_pos = 15

change_hat(Hats.Sunflower_Hat)

while True:
	if get_pos_x() == 0:
		h.plantGrass()
		move(North)

		if get_pos_y() == top_pos:
			h.plantGrass()
			h.moveToNext()
			
	elif get_pos_x() == 2 or get_pos_x() == 3 or get_pos_x() == 1:
		h.plantCarrot()
		move(North)
		
		if get_pos_y() == top_pos:
			h.plantCarrot()
			h.moveToNext()
			
	elif  get_pos_x() == 4:
		h.plantCactus()
		move(North)
		
		if get_pos_y() == top_pos:
			h.plantCactus()
			h.moveToNext()
		
			
	elif get_pos_x() == 5:
		h.plantSunflower()
		move(North)

		if get_pos_y() == top_pos:
			h.plantSunflower()
			h.moveToNext()
			
	elif get_pos_x() == 6 or get_pos_x() == 1:
		h.plantTree()
		move(North)

		if get_pos_y() == top_pos:
			h.plantTree()
			h.moveToNext()
			
	else:
		h.plantPumpkin()
		move(North)

		if get_pos_y() == top_pos:
			h.plantPumpkin()
			h.moveToNext()
			
				
	
		
		
