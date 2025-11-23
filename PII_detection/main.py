from PII_detection.data import synthetic_gen
from pathlib import Path as _Path
import json

CONFIG_PATH = "config/paths.json"
try:
	with open(CONFIG_PATH) as f:
		config = json.load(f)
except:
	raise FileNotFoundError(f"Config file '{CONFIG_PATH}' doesn't exists")

if __name__ == "__main__":
	log_path = _Path(config["LOG_FILE"])
	if log_path.exists() and log_path.is_file():
		log_path.unlink()
	synthetic_gen.synthetic_gen(log_path)