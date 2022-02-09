from core.consts import Resources
import json
import os
from core.models.music import Song
from typing import List


def parse_songs() -> List[Song]:
	songs_dir_path = Resources.songs_path
	songs_paths = os.listdir(songs_dir_path)

	songs = []
	for file in songs_paths:
		song_json = json.load(file)
		songs.append(Song(song_json[Resources.id], song_json[Resources.song_name], song_json[Resources.popularity]))

	return songs
