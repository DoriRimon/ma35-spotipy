import json
from typing import Dict

def get_data(path) -> Dict:
	return json.load(path)
