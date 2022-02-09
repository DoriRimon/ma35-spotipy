from core.consts import id, song_name, popularity, songs_path
import json
import os
from core.models.music import Song
from typing import List


def parse_songs() -> List[Song]:
	songs_dir_path = songs_path
	songs_paths = os.listdir(songs_dir_path)

	songs = []
	for file in songs_paths:
		song_json = json.load(file)
		songs.append(Song(song_json[id], song_json[song_name], song_json[popularity]))

	return songs
