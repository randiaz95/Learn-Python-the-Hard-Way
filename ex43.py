from ex43_engine import Map, Engine

if __name__ == "__main__":
	init_map = Map("central_corridor")
	game = Engine(init_map)
	game.play()