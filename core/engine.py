from core.consts import Resources
from core.models.music import Song
from core.storage import get_data
from core.storage.parse import parse_songs
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
		users = get_data(Resources.system_users_path)
		for id, user in users:
			if user[Resources.user_name] == user_name:
				if user[Resources.password] == password:
					self.user_id = id
					self.user = user
				else:
					raise IncorrectPasswordException

		if not self.user:
			raise UserNameDoesntExistException
