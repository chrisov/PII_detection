import sys
import os

SRC_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "src"))

sys.path.append(SRC_PATH)

import bank_statement as bs

if __name__ == "__main__":
	statement = bs.bank_statement()
	print(statement)

	