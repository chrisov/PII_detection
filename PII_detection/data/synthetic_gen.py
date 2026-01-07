import shutil
from pathlib import Path as _Path
from PII_detection.data.account import generateSyntheticBank
from PII_detection.data.pdfs import generate_pdfs
from PII_detection.config import load_json


def synthetic_gen(logfile, logger):
	'''
	Initializes the logger and generates the synthetic pdfs,
	based on the html files in the samples directory.
	'''

	data_config = load_json("data_config")

	OUTPUT_DIR = _Path(data_config["OUTPUT_DIR"])
	if OUTPUT_DIR.exists() and OUTPUT_DIR.is_dir():
		shutil.rmtree(OUTPUT_DIR)

	accounts = []
	for bank in data_config["BANKS"]:
		if bank["isReadyToRender"]:
			accounts.extend(generateSyntheticBank(bank, int(data_config["ITERATIONS"]), data_config["MERCHANTS"], data_config["INCOMES"]))

	total = len(accounts)
	if accounts:
		for i, acc in enumerate(accounts):
			index = i % int(data_config["ITERATIONS"]) + 1
			generate_pdfs(acc, index, data_config)
			if not logfile.exists():
				logfile.parent.mkdir(parents=True, exist_ok=True)
			logger.info(f"'{acc._name}_{index}' created successfully! ({i + 1}/{total})")
			print(f"'{acc._name}_{index}' created successfully! ({i + 1}/{total})")
	else:
		logger.error("Accounts list empty!")