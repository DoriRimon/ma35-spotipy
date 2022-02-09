from core.consts import system_users_path, user_name_key, password_key
from core.storage import get_data
from core.storage.parse import parse_songs, parse_user_playlists
from core.storage.write import write_user_playlist
from core.models.users import User

from core.errors.users import UserNameDoesntExistException, IncorrectPasswordException
from core.errors.playlists import PlaylistNotFoundException

from uuid import uuid4
from typing import List


class Engine:
	def __init__(self):
		self.user_id: str = None
		self.user: User = None
		self.songs = parse_songs()

	def login(self, user_name: str, password: str):
		users = get_data(system_users_path)
		for id, user in users.items():
			if user[user_name_key] == user_name:
				if user[password_key] == password:
					self.user_id = id
					self.user = user
				else:
					raise IncorrectPasswordException

		if not self.user:
			raise UserNameDoesntExistException

	def get_playlist(self, playlist_name: str):
		playlists = parse_user_playlists(self.user_id)
		for playlist in playlists:
			if playlist.name == playlist_name:
				return playlist

		raise PlaylistNotFoundException

	def create_playlist(self, playlist_name: str, songs: List[str] = None):
		playlist_id = str(uuid4())
		write_user_playlist(self.user_id, playlist_id, playlist_name, songs)
