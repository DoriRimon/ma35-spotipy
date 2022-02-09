from enum import Enum


class UserType(Enum):
	PREMIUM = "Premium"
	BASIC = "Basic"
	ARTIST = "Artist"


# file types
json = "json"

# paths
path_delimiter = "/"
resources_dir = "resources"
music_dir = "music"
songs_dir = "songs"
system_dir = "system"
users_dir = "users"
playlists_dir = "playlists"

songs_path = path_delimiter.join([resources_dir, music_dir, songs_dir])
system_users_path = path_delimiter.join([resources_dir, system_dir, "users"]) + "." + json

# base tokens
name_delimiter = "_"
song_base = "song"
playlist_base = "playlist"


# paths structure
def user_dir_path(user_id: str):
	return path_delimiter.join([resources_dir, users_dir, user_id])


def user_playlist_path(user_id: str, playlist_id: str):
	return path_delimiter.join(
		[user_dir_path(user_id), playlists_dir, playlist_base]) + \
	       name_delimiter + playlist_id + "." + json


def song_path(song_id: str):
	return path_delimiter.join([songs_path, song_base]) + \
	       name_delimiter + song_id + "." + json


# json keys
user_name_key = "user_name"
password_key = "password"
id = "id"
song_name = playlist_name = "name"
popularity = "popularity"
playlist_date = "last-changed-date"
playlist_songs = "songs"
track = "track"
