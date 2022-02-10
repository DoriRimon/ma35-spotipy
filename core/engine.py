from core.consts import system_users_path, logs_file_path, user_name_key, password_key, playlist_name_exists_msg, \
	basic_user_returned_results_limit, UserType, Logs, basic_user_playlist_creation_limit, \
	basic_user_playlist_songs_limit
from core.models.music import Album, Song
from core.storage import get_data
from core.storage.parse import parse_user_playlists, parse_all_users, parse_user, parse_albums
from core.storage.write import write_user_playlist

from core.models.users import BasicUser, Artist

from core.errors.users import UserNameDoesntExistException, IncorrectPasswordException, ArtistNotFoundException, \
	BasicUserInvalidCreationException
from core.errors.music import PlaylistNotFoundException, InvalidPlaylistNameException, AlbumNotFoundException

from uuid import uuid4
from typing import List

import logging
logging.basicConfig(filename=logs_file_path,
                    filemode="a",
                    format="%(asctime)s,%(msecs)d :: %(name)s :: %(levelname)s :: %(message)s",
                    datefmt="%H:%M:%S",
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)


def _limit_return_amount(getter_function):
	def limited_getter(self, *args):
		result = getter_function(self, *args)

		if self.user.user_type != UserType.BASIC.value:
			return result
		return result[:min(basic_user_returned_results_limit, len(result))]

	return limited_getter

def _limit_playlist_creation(creation_function):
	def blocked_creator(self, playlist_name, songs):
		cant_create = True
		if self.user.user_type != UserType.BASIC.value:
			cant_create = False
		elif len(parse_user_playlists(self.user.id)) < basic_user_playlist_creation_limit:
			cant_create = False
		elif len(songs) < basic_user_playlist_songs_limit:
			cant_create = False

		if cant_create:
			raise BasicUserInvalidCreationException
		return creation_function(self, playlist_name, songs)

	return blocked_creator


class Engine:
	def __init__(self):
		self.user_id: str = None
		self.user: BasicUser = None

	def login(self, user_name: str, password: str):
		users = get_data(system_users_path)
		for id, user in users.items():
			if user[user_name_key] == user_name:
				if user[password_key] == password:
					logger.info(Logs.login_successfully(user_name))
					self.user_id = id
					self.user = parse_user(id)
				else:
					logger.error(Logs.login_failed(user_name))
					raise IncorrectPasswordException

		if not self.user:
			logger.error(Logs.login_failed(user_name))
			raise UserNameDoesntExistException

	def get_playlist(self, playlist_name: str):
		playlists = parse_user_playlists(self.user_id)
		for playlist in playlists:
			if playlist.name == playlist_name:
				return playlist

		logger.error(Logs.search_failed("playlist"))
		raise PlaylistNotFoundException

	@_limit_playlist_creation
	def create_playlist(self, playlist_name: str, songs: List[str] = None):
		try:
			self.get_playlist(playlist_name)
			logger.error(Logs.creation_failed("playlist"))
			raise InvalidPlaylistNameException(playlist_name_exists_msg)
		except PlaylistNotFoundException as e:
			playlist_id = str(uuid4())
			write_user_playlist(self.user_id, playlist_id, playlist_name, songs)

	@_limit_return_amount
	def get_all_artists(self) -> List[Artist]:
		all_users = parse_all_users()
		return list(filter(lambda user: isinstance(user, Artist), all_users))

	@_limit_return_amount
	def get_artist_albums(self, artist_id) -> List[Album]:
		artists = self.get_all_artists()
		artist = list(filter(lambda a: a.id == artist_id, artists))
		if not artist:
			logger.error(Logs.search_failed("artist"))
			raise ArtistNotFoundException
		return artist[0].albums

	@_limit_return_amount
	def get_album_songs(self, album_id: str) -> List[Song]:
		all_albums = parse_albums()
		album = list(filter(lambda a: a.id == album_id, all_albums))
		if not album:
			logger.error(Logs.search_failed("album"))
			raise AlbumNotFoundException
		return album[0].songs

	@_limit_return_amount
	def get_artist_top_songs(self, artist_id: str, limit=10):
		albums = self.get_artist_albums(artist_id)  # returns albums limited by UserType
		songs = []
		for album in albums:
			songs += album.songs
		songs.sort(key=lambda song: song.popularity, reverse=True)
		return songs[:min(limit, len(songs))]

	def get_artist_id(self, artist_name: str) -> str:
		artists = self.get_all_artists()
		for artist in artists:
			if artist.name == artist_name:  # for now returns first artist found
				return artist.id

		raise ArtistNotFoundException

	@staticmethod
	def get_album_id(album_name: str) -> str:
		all_albums = parse_albums()
		for album in all_albums:
			if album.name == album_name:  # for now returns first album found
				return album.id

		raise AlbumNotFoundException
