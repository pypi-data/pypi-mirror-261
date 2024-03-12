#!/!usr/bin/env python
__program__ = "test_factorial"
__description__ = "test the factorial function" 
__date__ = "11/03/24"
__author__ = "Christophe Lagaillarde"
__version__ = "1.0"
__license__ = "MIT License"
__copyright__ = "Copyright (c) 2024 Christophe Lagaillarde"

import sys
sys.path.append('../')
from algo_fun.factorial import factorial

def test_factorial() -> None:
	
	assert factorial(1) == 1
	assert factorial(2) == 2
	assert factorial(3) == 6
	assert factorial(4) == 24
	assert factorial(5) == 120
	assert factorial(6) == 720
	assert factorial(7) == 5040
	assert factorial(8) == 40320
	assert factorial(9) == 362880
	assert factorial(10) == 3628800
		
	return None

if __name__ == '__main__':
	test_factorial()
