from PII_detection.data import synthetic_gen
from pathlib import Path as _Path
from PII_detection.config import load_json
from PII_detection.utils.logging import setup_logger

def init_logger(paths_config):
	"""
	Initializes the log directory and file.

	Parameters:
		paths_config: Contains all the config directories and files.

	Returns:

	"""
	log_path = (_Path(paths_config["LOG_FILE"])).resolve()
	log_path.parent.mkdir(parents=True, exist_ok=True)
	if log_path.exists() and log_path.is_file():
		log_path.unlink()
	logger = setup_logger("synthetic_gen.py", str(log_path))
	return (logger)


if __name__ == "__main__":
	paths_config = load_json("paths")
	log_file = init_logger(paths_config)
	log_path = (_Path(paths_config["LOG_FILE"])).resolve()
	synthetic_gen.synthetic_gen(log_path, log_file)