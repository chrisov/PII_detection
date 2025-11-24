from .account import generateSyntheticBank
from .pdfs import generate_pdfs
from ..utils.logging import setup_logger
from pathlib import Path as _Path
import shutil
import json

_this = _Path(__file__).resolve()
candidate = [
	_this.parent.parent / "config" / "data_config.json",  # PII_detection/config/data_config.json
	_this.parent / "config" / "data_config.json",         # PII_detection/data/config/data_config.json
	_this.parent.parent.parent / "config" / "data_config.json",  # repo_root/config/data_config.json
]
CONFIG_PATH = None
for p in candidate:
	if p.exists():
		CONFIG_PATH = p
		break


def synthetic_gen(logfile):
	
	logger = setup_logger("synthetic_gen.py", str(logfile))

	if CONFIG_PATH is None:
		tried = ", ".join(str(p) for p in candidate)
		logger.error(f"Config file doesn't exists: {tried}")
		raise FileNotFoundError()

	with open(CONFIG_PATH) as f:
		data_config = json.load(f)

	OUTPUT_DIR = _Path(data_config["OUTPUT_DIR"])
	if OUTPUT_DIR.exists() and OUTPUT_DIR.is_dir():
		shutil.rmtree(OUTPUT_DIR)

	accounts = []
	for bank in data_config["BANKS"]:
		if bank["isReadyToRender"]:
			accounts.extend(generateSyntheticBank(bank, int(data_config["ITERATIONS"])))

	total = len(accounts)
	if accounts:
		for i, acc in enumerate(accounts):
			index = i % int(data_config["ITERATIONS"]) + 1
			generate_pdfs(acc, index, data_config)
			if not logfile.exists():
				logfile.parent.mkdir(parents=True, exist_ok=True)
			logger.info(f"'{acc._name}_{index}' created successfully! ({i + 1}/{total})")
			print(acc._holder)
	else:
		logger.error("Accounts list empty!")