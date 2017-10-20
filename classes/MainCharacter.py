import logging as log

log.basicConfig(level=log.DEBUG)
# log.basicConfig(level=log.CRITICAL)

class MainCharacter:
	"""Class that define the main character properties :
		- name 
		- position
		- inventory"""

	NAME = "MacGyver"

	def __init__(self, pos_x, pos_y):
		self.position_x = pos_x
		self.position_y = pos_y
		self.inventory = []

	def move(self, direction):
		if direction == "up":
			self.position_y -= 1
		elif direction == "down":
			self.position_y += 1
		elif direction == "right":
			self.position_x += 1
		elif direction == "left":
			self.position_x -= 1
		else:
			log.debug("Error: can't move character - direction non recognized")

	def add_item(self, item):
		self.inventory.append(item)

def main()
	pass

if __name__ == "__main__":
	main()

