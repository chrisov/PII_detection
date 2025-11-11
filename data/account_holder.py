from faker import Faker
import colorama

fake = Faker()
colorama.init()

class account_holder:
	
	def __init__(self):
		self._name = fake.name()
		self._ssn = fake.ssn()
		self._address = fake.address()
		self._account_number = fake.bban()
		self._routing_number = fake.aba()
		self._phone_number = fake.phone_number()
		self._email = fake.email()
	
	def __repr__(self):
		res = f"{colorama.Fore.GREEN + 'Person ' + colorama.Style.RESET_ALL + '-' * 40}\n"
		res += f"{colorama.Fore.YELLOW}  Name{colorama.Style.RESET_ALL}: {self._name}\n"
		res += f"{colorama.Fore.YELLOW}  SSN{colorama.Style.RESET_ALL}: {self._ssn}\n"
		res += f"{colorama.Fore.YELLOW}  Acount number{colorama.Style.RESET_ALL}: {self._account_number}\n"
		res += f"{colorama.Fore.YELLOW}  Routing number{colorama.Style.RESET_ALL}: {self._routing_number}\n"
		res += f"{colorama.Fore.YELLOW}  Phone number{colorama.Style.RESET_ALL}: {self._phone_number}\n"
		res += f"{colorama.Fore.YELLOW}  Home address{colorama.Style.RESET_ALL}: {self._address}\n"
		res += f"{colorama.Fore.YELLOW}  Email address{colorama.Style.RESET_ALL}: {self._email}\n"
		res += f"{'-' * 40 + colorama.Fore.RED + ' Person' + colorama.Style.RESET_ALL}"
		return res

def generate_person():
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

# if __name__ == "__main__":
# 	person = account_holder()
# 	print(person)