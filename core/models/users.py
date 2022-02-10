from typing import List

from core.consts import UserType
from core.models.music import Album


class BasicUser:
	def __init__(self, id: str, name: str, user_type: UserType):
		self.id = id
		self.name = name
		self.user_type = user_type


class Artist(BasicUser):
	def __init__(self, id: str, name: str, albums: List[Album]):
		super().__init__(id, name, UserType.ARTIST)
		self.albums = albums
