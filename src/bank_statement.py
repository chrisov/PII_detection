import calendar as cal
import random as rd
import account_holder as holder
import colorama
from faker import Faker
from datetime import date
from tabulate import tabulate

fake = Faker()
colorama.init()

merchants = ['Amazon', 'Walmart', 'Shell Gas', 'Starbucks', 'ATM Withdrawal', 'GreenLeaf Grocers', 'City Central Market', 'QuickStop Pharmacy', 'Urban Outfitters P-O-S', 'The Hardware Hub Ltd.',			'Nebula Streaming Service', 'CloudCompute Hosting Fee', 'ProConnect Software Renewal', 'Monthly Mobile Bill - DataCom', 'Audible Books Platform', 
			'Bistro Firenze - Lunch', 'The Coffee Cart (Tap Payment)', 'CityCab Ride Share Service', 'Global Airlines Ticket Ref', 'Hotel Meridian Reservation', 
			'PowerGrid Electric Co. Payment', 'Metro Water Services (EFT)', 'SecureHome Insurance Premium', 'Monthly Rent Payment - Apt 4B', 'Waste Management Fee (Direct Debit)', 
			'ATM Withdrawal - City Branch', 'Inter-Bank Transfer (Savings)', 'Loan Repayment - Mortgage', 'Foreign Exchange Fee - USD', 'Dr. Anya Sharma (Medical Bill)',
			'AutoRepair Garage Visit', 'Public Transport Pass Top-Up', 'Charity Donation - Shelter Fund', 'Local Library Overdue Fine']

incomes = ['ACME Corp Payroll', 'Interest Payment', 'Transfer from Client Services Inc', 'Rental Income Deposit', 'Retailer Refund']

class bank_statement:

	def __init__(self):
		self._holder = holder.account_holder()
		self._month = rd.randint(1, 12)
		self._year = rd.randint(2015, 2025)
		self._issue_date = date(self._year, self._month, cal.monthrange(self._year, self._month)[1])
		self._balance = round(rd.uniform(1000, 10000), 2)
		self._history = self.generate_transactions()

	def generate_debit(self, num_transactions=rd.randint(2, 20)):
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
				"date": fake.date_between(
					start_date=date(self._year, self._month, 1),
					end_date=date(self._year, self._month, cal.monthrange(self._year, self._month)[1])),
				"merchant": rd.choice(merchants),
				"amount": round(rd.uniform(5, 500), 2),
				"type": "debit"
			})
		return transactions

	def	generate_credit(self, num_transactions=rd.randint(1, 4)):
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
				"date": fake.date_between(
					start_date=date(self._year, self._month, 1),
					end_date=date(self._year, self._month, cal.monthrange(self._year, self._month)[1])),
				"merchant": incomes[i],
				"amount": round(rd.uniform(300, 1000), 2),
				"type": "credit"
			})
		return transactions

	def generate_transactions(self):
		"""
		Generates a list of transactions for a person, with the following attributes:
		date, merchant, amount, account, type.

		Returns (list[dict]): A list of transactions.
		"""

		transactions = []
		debits = self.generate_debit()
		credits = self.generate_credit()
		salary = [{
			"date": date(self._year, self._month, 1),
			"merchant": incomes[0],
			"amount": round(rd.uniform(1000, 3000), 2),
			"type": "debit"
			}]
		transactions = [*salary, *debits, *credits]
		transactions.sort(key=lambda transaction: transaction["date"])
		return transactions

	def __repr__(self):
		res = f"{colorama.Fore.GREEN + "Bank Statement " + colorama.Style.RESET_ALL + "-" * 45}\n"
		res += f"{self._holder}\n"
		res += f"{colorama.Fore.YELLOW}Bank statement issue date{colorama.Style.RESET_ALL }: {self._issue_date}\n"
		res += f"{colorama.Fore.YELLOW}Account init balance{colorama.Style.RESET_ALL }: {self._balance}\n"
		res += f"{tabulate(self._history, headers="keys", tablefmt="pretty")}\n"
		res += f"{"-" * 45 + colorama.Fore.RED + " Bank Statement" + colorama.Style.RESET_ALL}"
		return res

# if __name__ == "__main__":

# 	statement = bank_statement()
# 	print(statement)