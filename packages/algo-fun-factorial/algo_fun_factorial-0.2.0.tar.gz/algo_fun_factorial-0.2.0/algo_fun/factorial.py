#!/!usr/bin/env python
__program__ = "factorial"
__description__ = "return the factorial of the number" 
__date__ = "11/03/24"
__author__ = "Christophe Lagaillarde"
__version__ = "2.0"
__license__ = "MIT License"
__copyright__ = "Copyright (c) 2024 Christophe Lagaillarde"

import sys

def factorial(number: int):

	try:
		result: int = 1
		
		if number < 0:
			raise ValueError("Factorial is undefined for negative numbers")	

		for i in range(1, number + 1):
			result *= i  

	except (ValueError ,TypeError):
		sys.exit("only accepting integer")

	return result


if __name__ == "__main__":	
	factorial(int(sys.argv[1]))

