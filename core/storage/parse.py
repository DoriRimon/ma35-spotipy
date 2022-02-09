from core.consts import id, song_name, popularity, songs_path, path_delimiter, track
import json
import os
from core.models.music import Song
from typing import List


def parse_songs() -> List[Song]:
	songs_dir_path = songs_path
	songs_paths = os.listdir(songs_dir_path)

	songs_paths = list(map(lambda song_path: songs_dir_path + path_delimiter + song_path, songs_paths))
	songs = []
	for file_path in songs_paths:
		with open(file_path) as file:
			song_json = json.load(file)
			song_json = song_json[track]
			songs.append(Song(song_json[id], song_json[song_name], song_json[popularity]))

	return songs
