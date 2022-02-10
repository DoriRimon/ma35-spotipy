from core.engine import Engine

from core.errors.users import *
from core.errors.music import *

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
		user_name = input(Console.build_input_message(Console.enter_user_name))
		password = input(Console.build_input_message(Console.enter_password))
		try:
			self.engine.login(user_name, password)
			self._create_home_menu().show()
		except IncorrectPasswordException as e:
			print(Console.incorrect_password)
		except UserNameDoesntExistException as e:
			print(Console.incorrect_username)

	def _create_home_menu(self) -> ConsoleMenu:
		home_menu = ConsoleMenu(Console.main_title, exit_option_text=Console.exit)

		create_playlist = FunctionItem(Console.create_playlist, self._create_playlist)
		get_artists = FunctionItem(Console.get_artists, self._get_artists)
		get_artist_albums = FunctionItem(Console.get_artist_albums, self._get_artist_albums)
		get_artist_top_songs = FunctionItem(Console.get_artist_top_songs, self._get_artist_top_songs)
		get_album_songs = FunctionItem(Console.get_album_songs, self._get_album_songs)

		home_menu.append_item(create_playlist)
		home_menu.append_item(get_artists)
		home_menu.append_item(get_artist_albums)
		home_menu.append_item(get_artist_top_songs)
		home_menu.append_item(get_album_songs)

		return home_menu

	def _create_playlist(self):
		playlist_name = input(Console.build_input_message(Console.enter_playlist_name))
		try:
			self.engine.create_playlist(playlist_name)
		except InvalidPlaylistNameException as e:
			print(Console.invalid_playlist_name)

	def _get_artists(self):
		artists = self.engine.get_all_artists()
		for artist in artists:
			print(artist.name)

	def _get_artist_albums(self):
		artist_name = input(Console.build_input_message(Console.enter_artist_name))
		try:
			artist_id = self.engine.get_artist_id(artist_name)
			albums = self.engine.get_artist_albums(artist_id)
			for album in albums:
				print(album.name)
		except ArtistNotFoundException as e:
			print(Console.artist_not_found)

	def _get_artist_top_songs(self):
		artist_name = input(Console.build_input_message(Console.enter_artist_name))
		try:
			artist_id = self.engine.get_artist_id(artist_name)
			top_songs = self.engine.get_artist_top_songs(artist_id)
			for song in top_songs:
				print(song.name)
		except ArtistNotFoundException as e:
			print(Console.artist_not_found)

	def _get_album_songs(self):
		album_name = input(Console.build_input_message(Console.enter_album_name))

		try:
			album_id = Engine.get_album_id(album_name)
			songs = self.engine.get_album_songs(album_id)
			for song in songs:
				print(song.name)
		except AlbumNotFoundException as e:
			print(Console.album_not_found)
