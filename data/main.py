# Synthetic data generation pipeline entry point
import json
from account import account

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
	# accounts.append(account(config["banks"][1]))

	for acc in accounts:	
		print(acc)