from core.consts import id_key, song_name_key, popularity_key, songs_path, \
	user_dir_path, playlists_dir, path_delimiter, track_key, \
	playlist_name_key, playlist_songs_key
import json
import os
from core.models.music import Song, Playlist
from typing import List, Dict


def parse_songs() -> List[Song]:
	songs_dir_path = songs_path
	songs_paths = os.listdir(songs_dir_path)

	songs_paths = list(map(lambda song_path: songs_dir_path + path_delimiter + song_path, songs_paths))
	songs = []
	for file_path in songs_paths:
		with open(file_path) as file:
			song_json = json.load(file)
			song_json = song_json[track_key]
			songs.append(Song(song_json[id],
			                  song_json[song_name_key],
			                  song_json[popularity_key]))

	return songs

def parse_user_playlists(user_id: str) -> List[Playlist]:
	playlists_dir_path = user_dir_path(user_id) + path_delimiter + playlists_dir
	playlists_paths = os.listdir(playlists_dir_path)

	playlists_paths = (list(map(lambda playlist_path: playlists_dir_path + path_delimiter + playlist_path, playlists_paths)))
	playlists = []
	for file_path in playlists_paths:
		with open(file_path) as file:
			playlist_json = json.load(file)
			playlists.append(Playlist(playlist_json[id_key],
			                          playlist_json[playlist_name_key],
			                          playlist_json[playlist_songs_key]))

	return playlists
