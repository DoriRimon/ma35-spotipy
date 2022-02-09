from enum import Enum


class UserType(Enum):
	PREMIUM = "Premium"
	BASIC = "Basic"
	ARTIST = "Artist"


class Resources(Enum):
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
	def user_dir_path(self, user_id: str):
		return self.path_delimiter.join(self.resources_dir, self.users_dir)

	def user_playlist_path(self, user_id: str, playlist_id: str):
		return self.path_delimiter.join(
			[self.user_dir_path(user_id), self.playlists_dir, self.playlist_base]) + \
		       self.name_delimiter + playlist_id + "." + self.json

	def song_path(self, song_id: str):
		return self.path_delimiter.join([self.songs_path, self.song_base]) + \
		       self.name_delimiter + song_id + "." + self.json

	# json keys
	user_name = "user_name"
	password = "password"
