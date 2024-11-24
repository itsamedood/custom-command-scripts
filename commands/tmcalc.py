def calculateTilemapImageSize() -> list:
	"""
	Calculates the image size to make a tilemap with:

	w = `Width of tiles`

	h = `Height of tiles`

	r = `Amount of rows`

	c = `Amount of tiles per column`

	And returns:

	iw = `Image Width`

	ih = `Image Height`
	"""

	while True:
		w = input("How wide are the tiles? ")
		try:
			w = int(w)
			break
		except: print("That's not a number!")

	while True:
		h = input("How high are the tiles? ")
		try:
			h = int(h)
			break
		except: print("That's not a number!")

	while True:
		r = input("How many tiles per row? ")
		try:
			r = int(r)
			break
		except: print("That's not a number!")

	while True:
		c = input("How many tiles in each column? ")
		try:
			c = int(c)
			break
		except: print("That's not a number!")

	iw = w * r
	ih = h * c
	return [iw, ih]


print(calculateTilemapImageSize())
