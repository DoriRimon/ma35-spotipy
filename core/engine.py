from core.consts import system_users_path
from core.storage import get_data
from core.storage.parse import parse_songs
from core.storage.write import write_user_playlist
from core.models.users import User
from core.errors.users import UserNameDoesntExistException, IncorrectPasswordException
from uuid import uuid4
from typing import List


class Engine:
	def __init__(self):
		self.user_id: str = None
		self.user: User = None
		self.songs = parse_songs()

	def login(self, user_name: str, password: str):
		users = get_data(system_users_path)
		for id, user in users:
			if user[user_name] == user_name:
				if user[password] == password:
					self.user_id = id
					self.user = user
				else:
					raise IncorrectPasswordException

		if not self.user:
			raise UserNameDoesntExistException

	def create_playlist(self, playlist_name: str, songs: List[str] = None):
		playlist_id = str(uuid4())
		write_user_playlist(self.user_id, playlist_id, playlist_name, songs)
