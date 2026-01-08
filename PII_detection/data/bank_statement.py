import calendar as cal
import random as rd
import colorama
from datetime import date, timedelta, datetime
from tabulate import tabulate

colorama.init()

class statement:

	def __init__(self, synthetic_info, merchants, incomes):
		self._month = rd.randint(1, 12)
		self._year = rd.randint(2015, 2025)
		self._issue_date = date(self._year, self._month, cal.monthrange(self._year, self._month)[1]).strftime("%d %b %Y")
		self._balance = round(rd.uniform(3000, 10000), 2)
		self._history = self.generate_transactions(synthetic_info, merchants, incomes)
		self._previous_date = (datetime.strptime(self._history[0]["date"], "%d %b %Y") - timedelta(days=1)).strftime("%d %b %Y")
		self._last_statement_date = self._history[-1]["date"]
		self.calculate_balances()
		print(self)



	def generate_debit(self, synthetic_info, merchants, num_transactions=rd.randint(5, 8)):
		"""
		Generates a list of debit transactions for a person, with the following attributes:
		date, merchant, amount, account, type.

		Args: 
			num_transactions: Size of the generated list (default=rd(2, 20)).

		Returns (list[dict]): A list of debit transactions.
		"""

		transactions = []
		for _ in range(num_transactions):
			transactions.append({
				"date": synthetic_info.date_between(
					start_date=date(self._year, self._month, 1),
					end_date=date(self._year, self._month, cal.monthrange(self._year, self._month)[1])),
				"merchant": rd.choice(merchants),
				"debit": round(rd.uniform(5, 500), 2),
			})
		return transactions



	def	generate_credit(self, synthetic_info, incomes, num_transactions=rd.randint(1, 4)):
		"""
		Generates a list of credit transactions for a person, with the following attributes:
		date, merchant, amount, account, type.

		Args: 
			num_transactions: Size of the generated list (default=rd(1, 4)). 

		Returns (list[dict]): A list of credit transactions.
		"""
		transactions = []
		for i in range(1, num_transactions):
			transactions.append({
				"date": synthetic_info.date_between(
					start_date=date(self._year, self._month, 1),
					end_date=date(self._year, self._month, cal.monthrange(self._year, self._month)[1])),
				"merchant": incomes[i],
				"credit": round(rd.uniform(300, 1000), 2),
			})
		return transactions



	def generate_transactions(self, synthetic_info, merchants, incomes):
		"""
		Generates a list of transactions for a person, with the following attributes:
		date, merchant, amount, account, type.

		Returns (list[dict]): A list of transactions.
		"""

		balance = {
			"date": date(self._year, self._month, 1),
			"merchant": "BALANCE B/F",
			"credit": "",
			"debit": "",
			"balance": self._balance,
			}
		debits = self.generate_debit(synthetic_info, merchants)
		credits = self.generate_credit(synthetic_info, incomes)
		salary = [{
			"date": date(self._year, self._month, 1),
			"merchant": incomes[0],
			"credit": round(rd.uniform(1000, 3000), 2),
			}]
		transactions = [*salary, *debits, *credits]
		transactions.sort(key=lambda transaction: transaction["date"])
		transactions.insert(0, balance)
		for t in transactions:
			t["date"] = t["date"].strftime("%d %b %Y")
		return transactions
	


	def	calculate_balances(self):
		"""
		Calculates the balances column in the statement and stores them in the history.
		"""

		history = self._history
		for i, item in enumerate(history):
			if i == 0:
				item["balance"] = self._balance
			else:
				previous_balance = history[i - 1]["balance"]
				if 'credit' in item:
					item["balance"] = round(previous_balance + item["credit"], 2)
				else:
					item["balance"] = round(previous_balance - item["debit"], 2)
	

	def calculate_total_debits(self):
		"""
		Calculates and returns the statement's total debits.
		"""
	
		result = 0.0
		for item in self._history:
			try:
				result += float(item.get("debit", 0) or 0)
			except (ValueError, TypeError):
				pass
		return round(result, 2)



	def calculate_total_credits(self):
		"""
		Calculates and returns the statement's total credits.
		"""

		result = 0.0
		for item in self._history:
			try:
				result += float(item.get("credit", 0) or 0)
			except (ValueError, TypeError):
				pass
		return round(result, 2)



	def __repr__(self):
		res = f"{colorama.Fore.GREEN}Bank Statement {colorama.Style.RESET_ALL}{'-' * 45}\n"
		res += f"{colorama.Fore.YELLOW}Issue date{colorama.Style.RESET_ALL}: {self._issue_date}\n"
		res += f"{colorama.Fore.YELLOW}Init balance{colorama.Style.RESET_ALL}: {self._balance}\n"
		res += tabulate(self._history, headers="keys", tablefmt="pretty") + "\n"
		res += f"{'-' * 45 + colorama.Fore.RED + ' Bank Statement' + colorama.Style.RESET_ALL}"
		return res



if __name__ == "__main__":
	statement = statement()
	print(statement)