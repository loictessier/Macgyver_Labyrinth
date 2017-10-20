#! /usr/bin/env python3
# coding: utf-8
import MainCharacter as mc
import Board as bo

class Game:

	def __init__(self):
		self.main_character = mc.MainCharacter(1,8)
		self.board = bo.Board()
		self.board.create_board_map_from_file("level1.map")

def main():
	pass

if __name__ == "__main__":
	main()