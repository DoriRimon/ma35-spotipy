from core.consts import Resources
from core.storage import get_data
from core.storage.parse import Parser
from core.models.users import User
from core.errors.users import UserNameDoesntExistException, IncorrectPasswordException

class Engine:
	def __init__(self):
		self.user_id: str = None
		self.user: User = None
		self.songs = Parser.parse_songs()

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
