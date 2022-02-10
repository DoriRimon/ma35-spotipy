from core.engine import Engine

def main():
	engine = Engine()
	print(list(map(lambda song: song.name, engine.songs)))

	engine.login("dori", "Ma!123456")
	# engine.create_playlist("top_pop")
	print(list(map(lambda artist: artist.name, engine.get_all_artists())))
	print(engine.get_artist_albums("user_2wp6i8BxLF3UrF1J3LY4WC"))


if __name__ == "__main__":
	main()
