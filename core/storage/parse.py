from core.consts import UserType, id_key, name_key, popularity_key, songs_path, \
	user_dir_path, playlists_dir, path_delimiter, track_key, \
	name_key, playlist_songs_key, resources_dir, users_dir, metadata_file, json_type, type_key, albums_key

import json
import os

from core.models.music import Song, Playlist
from core.models.users import BasicUser, Artist

from typing import List

# TODO - separate duplicate code in parse_songs and parse_user_playlists

def parse_songs() -> List[Song]:
	songs_dir_path = songs_path
	songs_paths = os.listdir(songs_dir_path)

	songs_paths = list(map(lambda song_path: songs_dir_path + path_delimiter + song_path, songs_paths))
	songs = []
	for file_path in songs_paths:
		with open(file_path) as file:
			song_json = json.load(file)
			song_json = song_json[track_key]
			songs.append(Song(song_json[id_key],
			                  song_json[name_key],
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
			                          playlist_json[name_key],
			                          playlist_json[playlist_songs_key]))

	return playlists

def parse_all_users():
	users_dir_path = path_delimiter.join([resources_dir, users_dir])
	users_metadata_paths = [path_delimiter.join([
		users_dir_path,
		inner,
		metadata_file]) + "." + json_type for inner in os.listdir(users_dir_path)]

	users = []
	for file_path in users_metadata_paths:
		with open(file_path) as file:
			user_json = json.load(file)
			user_type = user_json[type_key]
			if user_type == UserType.PREMIUM.value or user_type == UserType.BASIC.value:
				users.append(BasicUser(
					user_json[id_key],
					user_json[name_key],
					user_type
				))
			else:
				users.append(Artist(
					user_json[id_key],
					user_json[name_key],
					user_json[albums_key]
				))

	return users
