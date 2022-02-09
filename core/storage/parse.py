from core.consts import Resources
import json
import os
from core.models.music import Song
from typing import List


class Parser:
	@staticmethod
	def parse_songs() -> List[Song]:
		songs_dir_path = Resources.songs_path
		songs_paths = os.listdir(songs_dir_path)

		songs_paths = list(map(lambda song_path: songs_dir_path + Resources.path_delimiter + song_path, songs_paths))
		songs = []
		for file_path in songs_paths:
			with open(file_path) as file:
				song_json = json.load(file)
				song_json = song_json[Resources.track]
				songs.append(Song(song_json[Resources.id], song_json[Resources.song_name], song_json[Resources.popularity]))

		return songs
