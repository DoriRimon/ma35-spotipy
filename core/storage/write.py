from typing import List
from core.consts import id_key, playlist_name_key, playlist_date_key, playlist_songs_key, user_playlist_path
import time
import json


def write_user_playlist(user_id: str, playlist_id: str, playlist_name: str,
                        songs: List[str]):
	playlist_dict = {id_key: playlist_id,
	                 playlist_name_key: playlist_name,
	                 playlist_date_key: time.asctime(),
	                 playlist_songs_key: songs}

	path = user_playlist_path(user_id, playlist_id)
	with open(path, 'w') as file:
		json.dump(playlist_dict, file)
