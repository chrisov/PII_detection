from .account import generateSyntheticBank
from colorama import Fore, Style
from .pdfs import generatePDFs
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

if CONFIG_PATH is None:
	tried = ", ".join(str(p) for p in candidate)
	raise FileNotFoundError(f"Config file not found. Tried: {tried}")

with open(CONFIG_PATH) as f:
	config = json.load(f)


def synthetic_gen():

	OUTPUT_DIR = _Path(config["OUTPUT_DIR"])
	if OUTPUT_DIR.exists() and OUTPUT_DIR.is_dir():
		shutil.rmtree(OUTPUT_DIR)

	accounts = []
	for bank in config["BANKS"]:
		if bank["isReadyToRender"]:
			accounts.extend(generateSyntheticBank(bank, int(config["ITERATIONS"])))

	total = len(accounts)
	if accounts:
		for i, acc in enumerate(accounts):
			index = i % int(config["ITERATIONS"]) + 1
			generatePDFs(acc, index, config)
			print(f"'{Fore.YELLOW}{acc._name}_{index}{Style.RESET_ALL}' created {Fore.GREEN}successfully{Style.RESET_ALL}! ({i + 1}/{total})")
			# print(acc._statement)
	else:
		print("Accounts list empty!")