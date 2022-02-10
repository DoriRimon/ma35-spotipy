from core.consts import UserType, id_key, name_key, popularity_key, songs_path, \
	user_dir_path, playlists_dir, path_delimiter, track_key, \
	name_key, playlist_songs_key, resources_dir, users_dir, metadata_file, json_type, type_key, albums_key

import json
import os

from core.models.music import Song, Playlist
from core.models.users import BasicUser, Artist

from typing import List

# TODO - separate duplicate code in parse_songs and parse_user_playlists

def dir_paths(dir_path) -> List[str]:
	inner_paths = os.listdir(dir_path)
	return list(map(lambda path: dir_path + path_delimiter + path, inner_paths))

def parse_songs() -> List[Song]:
	songs_paths = dir_paths(songs_path)
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
	playlists_paths = dir_paths(playlists_dir_path)
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

def parse_user(user_id: str):
	all_users = parse_all_users()
	user = list(filter(lambda u: u.id == user_id, all_users))
	if not user:
		return None
	return user[0]
