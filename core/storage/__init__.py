import json
from typing import Dict

def get_data(path) -> Dict:
	with open(path) as file:
		return json.load(file)
