import colorama

colorama.init()

class bank_client:
	
	def __init__(self, synthetic_info):
		self._name = synthetic_info.name()
		self._gender = synthetic_info.random_element(elements=('Male', 'Female'))
		self._ssn = synthetic_info.ssn()
		self._address = synthetic_info.address()
		self._routing_number = synthetic_info.aba()
		self._phone_number = synthetic_info.phone_number()
		self._email = synthetic_info.email()
	
	def __repr__(self):
		res = f"{colorama.Fore.GREEN + 'Person ' + colorama.Style.RESET_ALL + '-' * 40}\n"
		res += f"{colorama.Fore.YELLOW}  Name{colorama.Style.RESET_ALL}: {self._name}\n"
		res += f"{colorama.Fore.YELLOW}  SSN{colorama.Style.RESET_ALL}: {self._ssn}\n"
		res += f"{colorama.Fore.YELLOW}  Routing number{colorama.Style.RESET_ALL}: {self._routing_number}\n"
		res += f"{colorama.Fore.YELLOW}  Phone number{colorama.Style.RESET_ALL}: {self._phone_number}\n"
		add = (self._address).replace("\n", " ")
		res += f"{colorama.Fore.YELLOW}  Home address{colorama.Style.RESET_ALL}: {add}\n"
		res += f"{colorama.Fore.YELLOW}  Email address{colorama.Style.RESET_ALL}: {self._email}\n"
		res += f"{'-' * 40 + colorama.Fore.RED + ' Person' + colorama.Style.RESET_ALL}"
		return res
