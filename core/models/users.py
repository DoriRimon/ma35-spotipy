from typing import List

from core.consts import UserType
from core.models.music import Album


class User:
	def __init__(self, id: str, name: str):
		self.id = id
		self.name = name


class BasicUser(User):
	def __int__(self, id: str, name: str, type: UserType):
		super().__init__(id, name)
		self.type = type


class Artist(User):
	def __init__(self, id: str, name: str, albums: List[Album]):
		super().__init__(id, name)
		self.type = UserType.ARTIST
		self.albums = albums
