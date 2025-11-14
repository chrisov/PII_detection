# Synthetic data generation pipeline entry point
import json
from account import account
from synthetic_gen import generate_pdfs


CONFIG_PATH = "config/config.json"
try:
	with open(CONFIG_PATH) as f:
		config = json.load(f)
except:
	raise FileNotFoundError(f"Config file not found: {CONFIG_PATH}")

if __name__ == "__main__":
	accounts = []
	# for bank in config["banks"]:
	# 	accounts.append(account(bank))
	accounts.append(account(config["banks"][0]))
	
	for acc in accounts:
		generate_pdfs(acc)
		print(acc)