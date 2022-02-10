from enum import Enum


class UserType(Enum):
	PREMIUM = "Premium"
	BASIC = "Basic"
	ARTIST = "Artist"


# file types
json_type = "json"

# paths
path_delimiter = "/"
resources_dir = "resources"
music_dir = "music"
songs_dir = "songs"
system_dir = "system"
users_dir = "users"
playlists_dir = "playlists"
metadata_file = "metadata"

songs_path = path_delimiter.join([resources_dir, music_dir, songs_dir])
system_users_path = path_delimiter.join([resources_dir, system_dir, "users"]) + "." + json_type

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
	       name_delimiter + playlist_id + "." + json_type


def song_path(song_id: str):
	return path_delimiter.join([songs_path, song_base]) + \
	       name_delimiter + song_id + "." + json_type


# json keys
user_name_key = "user_name"
password_key = "password"
id_key = "id"
name_key = "name"
popularity_key = "popularity"
playlist_date_key = "last-changed-date"
playlist_songs_key = "songs"
track_key = "track"
type_key = "type"
albums_key = "albums"


# exceptions messages
playlist_name_exists_msg = "A playlist with the same name already exists"
