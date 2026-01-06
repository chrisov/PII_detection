from colorama import init, Fore, Style
from faker import Faker
from PII_detection.data.account_holder import bank_client
from PII_detection.data.bank_statement import statement

init()

class account:
	
	def __init__(self, bank):
		synthetic_info = Faker(bank["origin"])
		self._name = bank["name"]
		self._bic = bank["BIC"]
		self._holder = bank_client(synthetic_info)
		self._statement = statement(synthetic_info)
		self._iban = synthetic_info.bban()


	def __repr__(self):
		res = f"\n{Fore.GREEN + 'Bank account ' + Style.RESET_ALL + '-' * 40}\n"
		res += f"{Fore.YELLOW}Name{Style.RESET_ALL}: {self._name}\n"
		res += f"{Fore.YELLOW}BIC SWIFT{Style.RESET_ALL}: {self._bic}\n"
		res += f"{Fore.YELLOW}Iban{Style.RESET_ALL}: {self._iban}\n"
		res += f"{self._holder}\n"
		res += f"{'-' * 40 + Fore.RED + ' Bank account' + Style.RESET_ALL}"
		return res
		

def	generateSyntheticBank(bank, iterations) -> list:
	accounts = []
	for i in range(iterations):
		accounts.append(account(bank))
	return accounts
