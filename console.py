from core.engine import Engine

from core.errors.users import *

from core.consts import Console

from consolemenu import *
from consolemenu.items import *


# TODO - magic strings
class SpotipyConsole:
	def __init__(self):
		self.engine = Engine()

	def show(self):
		self._create_login_menu().show()

	def _create_login_menu(self) -> ConsoleMenu:
		login_menu = ConsoleMenu(Console.main_title, exit_option_text=Console.exit)

		login = FunctionItem(Console.login, self._login)
		login_menu.append_item(login)

		return login_menu

	def _login(self):
		user_name = input(Console.enter_user_name)
		password = input(Console.enter_password)
		try:
			self.engine.login(user_name, password)
			self._create_home_menu().show()
		except IncorrectPasswordException as e:
			print(Console.incorrect_password)
		except UserNameDoesntExistException as e:
			print(Console.incorrect_username)
