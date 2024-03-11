#!/!usr/bin/env python
__program__ = "add"
__description__ = "make the addition of all arguments" 
__date__ = "05/03/24"
__author__ = "Christophe Lagaillarde"
__version__ = "1.0"
__license__ = "MIT License"
__copyright__ = "Copyright (c) 2024 Christophe Lagaillarde"

import sys

def is_terminal_input(args: tuple) -> bool:

	try:
		return ".py" in args[0][0]

	except TypeError:
		return False

def add(*args) -> int:
	result: int = 0	

	if is_terminal_input(args):
		args: list[int] = [int(arg) for arg in args[0][1::]]
	else:
		args: list[int] = list(args)

	try:
		for arg in args:
			result += arg
	
	except ValueError:
		sys.exit("Only accepting integers")
	
	print(result)

	return result 



if __name__ == "__main__":
	add(sys.argv)

