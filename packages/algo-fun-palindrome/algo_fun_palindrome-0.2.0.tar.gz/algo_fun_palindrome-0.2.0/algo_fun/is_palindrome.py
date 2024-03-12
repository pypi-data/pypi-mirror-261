#!/!usr/bin/env python
__program__ = "is_palindrome"
__description__ = "say if string is a palindrome or not" 
__date__ = "12/03/24"
__author__ = "Christophe Lagaillarde"
__version__ = "2.0"
__license__ = "MIT License"
__copyright__ = "Copyright (c) 2024 Christophe Lagaillarde"

import sys

def is_palindrome(string: str) -> bool:
	return string == string[::-1]


if __name__ == "__main__":
	is_palindrome(sys.argv[1])
