from faker import Faker
import random
from datetime import date
import calendar

fake = Faker()

merchants = ['Amazon', 'Walmart', 'Shell Gas', 'Starbucks', 'ATM Withdrawal', 'GreenLeaf Grocers', 'City Central Market', 'QuickStop Pharmacy', 'Urban Outfitters P-O-S', 'The Hardware Hub Ltd.',			'Nebula Streaming Service', 'CloudCompute Hosting Fee', 'ProConnect Software Renewal', 'Monthly Mobile Bill - DataCom', 'Audible Books Platform', 
			'Bistro Firenze - Lunch', 'The Coffee Cart (Tap Payment)', 'CityCab Ride Share Service', 'Global Airlines Ticket Ref', 'Hotel Meridian Reservation', 
			'PowerGrid Electric Co. Payment', 'Metro Water Services (EFT)', 'SecureHome Insurance Premium', 'Monthly Rent Payment - Apt 4B', 'Waste Management Fee (Direct Debit)', 
			'ATM Withdrawal - City Branch', 'Inter-Bank Transfer (Savings)', 'Loan Repayment - Mortgage', 'Foreign Exchange Fee - USD', 'Dr. Anya Sharma (Medical Bill)',
			'AutoRepair Garage Visit', 'Public Transport Pass Top-Up', 'Charity Donation - Shelter Fund', 'Local Library Overdue Fine']

incomes = ['ACME Corp Payroll', 'Interest Payment', 'Transfer from Client Services Inc', 'Rental Income Deposit', 'Retailer Refund']

class bank_statement:

	def __init__(self):
		self._person = self.generate_person()
		self._month = random.randint(1, 12)
		self._year =random.randint(2015, 2025)
		self._balance = round(random.uniform(1000, 100000), 2)
		self._transactions = self.generate_transactions()

	def generate_person(self):
		"""
		Generates a person's profile, with the following attributes:
		name, ssn, address, bban, aba, phone number, email.

		Returns (dict): The person's profile.
		
		# NOTE: Phone number sometimes consists of letters/dots
		"""

		return {
			'name': fake.name(),
			'ssn': fake.ssn(),
			'address': fake.address(),
			'account_number': fake.bban(),
			'routing_number': fake.aba(),
			'phone': fake.phone_number(),
			'email': fake.email()
		}

	def generate_debit(self, num_transactions=random.randint(2, 20)):
		"""
		Generates a list of debit transactions for a person, with the following attributes:
		date, merchant, amount, account, type.

		Args: 
			num_transactions: Size of the generated list (default=random(2, 20)).

		Returns (list[dict]): A list of debit transactions.
		"""

		transactions = []
		for _ in range(num_transactions):
			transactions.append({
				'date': fake.date_between(
					start_date=date(self._year, self._month, 1),
					end_date=date(self._year, self._month, calendar.monthrange(self._year, self._month)[1])),
				'merchant': random.choice(merchants),
				'amount': round(random.uniform(5, 500), 2),
				'type': 'debit'
			})
		return transactions

	def	generate_credit(self, num_transactions=random.randint(1, 4)):
		"""
		Generates a list of credit transactions for a person, with the following attributes:
		date, merchant, amount, account, type.

		Args: 
			num_transactions: Size of the generated list (default=random(1, 4)). 

		Returns (list[dict]): A list of credit transactions.
		"""
		transactions = []
		for i in range(1, num_transactions):
			transactions.append({
				'date': fake.date_between(
					start_date=date(self._year, self._month, 1),
					end_date=date(self._year, self._month, calendar.monthrange(self._year, self._month)[1])),
				'merchant': incomes[i],
				'amount': round(random.uniform(300, 1000), 2),
				'type': 'credit'
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
			'date': date(self._year, self._month, 1),
			'merchant': incomes[0],
			'amount': round(random.uniform(1000, 3000), 2),
			'type': 'debit'
			}]
		transactions = [*salary, *debits, *credits]
		transactions.sort(key=lambda transaction: transaction["date"])
		return transactions


if __name__ == "__main__":

	account = bank_statement()

	print("Person\n" + "-" * 30)
	for key,value in account._person.items():
		print(f"'{key}': {value}")
	print("-" * 30 + "\n")

	print(f"Transactions ({len(account._transactions)})\n" + "-" * 30)
	for item in account._transactions:
		for key,value in item.items():
			print(f"'{key}': {value}")
		print("\n")
	print("-" * 30 + "\n")