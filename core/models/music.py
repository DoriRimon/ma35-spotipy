from typing import List

class MusicObject:
	def __init__(self, id: str, name: str):
		self.id = id
		self.name = name

class Song(MusicObject):
	def __init__(self, id: str, name: str, popularity: int):
		super().__init__(id, name)
		self.popularity = popularity
