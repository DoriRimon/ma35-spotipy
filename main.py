from core.engine import Engine

def main():
	engine = Engine()
	print(list(map(lambda song: song.name, engine.songs)))

	engine.login("dori", "Ma!123456")


if __name__ == "__main__":
	main()