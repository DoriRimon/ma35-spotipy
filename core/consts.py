from enum import Enum


class UserType(Enum):
	PREMIUM = "Premium"
	BASIC = "Basic"
	ARTIST = "Artist"


# limits
basic_user_returned_results_limit = 5
basic_user_playlist_creation_limit = 5
basic_user_playlist_songs_limit = 20

# file types
json_type = "json"

# paths
path_delimiter = "/"
resources_dir = "resources"
music_dir = "music"
songs_dir = "songs"
albums_dir = "albums"
system_dir = "system"
users_dir = "users"
playlists_dir = "playlists"
metadata_file = "metadata"

logs_file_path = path_delimiter.join([resources_dir, system_dir, "logs"]) + "." + "log"

songs_path = path_delimiter.join([resources_dir, music_dir, songs_dir])
albums_path = path_delimiter.join([resources_dir, music_dir, albums_dir])
system_users_path = path_delimiter.join([resources_dir, system_dir, "users"]) + "." + json_type

# base tokens
name_delimiter = "_"
song_base = "song"
playlist_base = "playlist"
user_base = "user"


# paths structure
def user_dir_path(user_id: str):
	return path_delimiter.join([resources_dir, users_dir, user_base]) + name_delimiter + user_id


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
songs_key = "songs"

# exceptions messages
playlist_name_exists_msg = "A playlist with the same name already exists"


# logs messages
class Logs:
	@staticmethod
	def login_successfully(user_name: str) -> str:
		return f"{user_name} logged in successfully"

	@staticmethod
	def login_failed(user_name: str) -> str:
		return f"login failed for user: {user_name}"

	@staticmethod
	def search_failed(search_type=None):
		if search_type:
			return f"search attempt of type {search_type} failed"
		return "search attempt failed"

	@staticmethod
	def write_successfully(write_type=None):
		if write_type:
			return f"written system object of type {write_type} successfully to disk"
		return "written successfully to disk"

	@staticmethod
	def creation_failed(creation_type=None):
		if creation_type:
			return f"creation of system object of type {creation_type} failed"
		return "creation of system object"


class Console:
	# titles
	main_title = "Spotipy Console"

	# options names
	exit = "Exit"
	login = "Login"

	create_playlist = "Create a new playlist"
	get_artists = "Show all artists"
	get_artist_albums = "Show artist's albums"
	get_artist_top_songs = "Show top 10 songs by artist"
	get_album_songs = "Show album's songs"

	# messages
	enter_user_name = "Please enter your user name"
	enter_password = "Please enter your password"

	enter_playlist_name = "Please enter playlist's name"
	enter_artist_name = "Enter artist name"
	enter_album_name = "Enter album name"

	# errors
	incorrect_password = "Incorrect password"
	incorrect_username = "Username doesn't exist"

	invalid_playlist_name = "Invalid playlist name"

	artist_not_found = "No such artist exists"
	album_not_found = "No such album"

	@staticmethod
	def build_input_message(message):
		return f"{message}: "
