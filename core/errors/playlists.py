class InvalidPlaylistNameException(Exception):
	def __init__(self, msg):
		super().__init__(msg)


class PlaylistNotFoundException(Exception):
	pass
