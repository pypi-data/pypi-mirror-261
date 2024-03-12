#!/!usr/bin/env python
__program__ = "test_is_palindrome"
__description__ = "Test the palindrome function" 
__date__ = "12/03/24"
__author__ = "Christophe Lagaillarde"
__version__ = "2.0"
__license__ = "MIT License"
__copyright__ = "Copyright (c) 2024 Christophe Lagaillarde"

import sys
sys.path.append('../')
from algo_fun.is_palindrome import is_palindrome

def test_is_palindrome() -> None:

	assert is_palindrome("a") is True 
	assert is_palindrome("tattarrattat") is True 
	assert is_palindrome("aibohphobia") is True 
	assert is_palindrome("step on no pets") is True 
	assert is_palindrome("vocabulary") is False
	assert is_palindrome("cupcake in the fridge") is False 
	
	return None


if __name__ == '__main__':
	test_is_palindrome()
