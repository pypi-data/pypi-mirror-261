#!/!usr/bin/env python
__program__ = "test_add"
__description__ = "test the addition function" 
__date__ = "05/03/24"
__author__ = "Christophe Lagaillarde"
__version__ = "1.0"
__license__ = "MIT License"
__copyright__ = "Copyright (c) 2024 Christophe Lagaillarde"

import sys
sys.path.append('../')
from algo_fun.add import add

def test_add() -> None:
	assert add(4, 5) == 9, "4 plus 5 does not equal 9"
	assert add(-8, -10) == -18, "-8 plus -10 does not equal -18"
	assert add(-50 ,33) == -17 , "-50 plus 33 does not equal -17"
	assert add(-25, 42, -5) == 12 , "-25 plus 42 plus -5 does not equal 12"
	
	return None

if __name__ == '__main__':
	test_add()
