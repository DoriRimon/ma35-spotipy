from typing import List
from core.consts import playlist_name, playlist_date, playlist_songs, user_playlist_path
import time
import json


def write_user_playlist(user_id: str, playlist_id: str, playlist_name: str,
                        songs: List[str]):
	playlist_dict = {playlist_name: playlist_name,
	                 playlist_date: time.asctime(),
	                 playlist_songs: songs}

	path = user_playlist_path(user_id, playlist_id)
	json.dump(playlist_dict, path)
