#!/usr/bin/env python3

# the filename should always start with test_xxx.py

import pytest
import calc

# !!! test function name is required to have 'test_' suffix
def test_add():
	assert calc.add(10, 5) == 15
	assert calc.add(-1, 1) == 0
	assert calc.add(-2, -3) == -5
	
	# a special Context Manager syntax
	with pytest.raises(TypeError):
		calc.add('2', 5)
		
def test_subtract():
	assert calc.subtract(10, 5) == 5
	assert calc.subtract(-1, 1) == -2
	assert calc.subtract(-2, -3) == 1

def test_multiply():
	assert calc.multiply(10, 5) == 50
	assert calc.multiply(-1, 1) == -1
	assert calc.multiply(-2, -3) == 6

def test_divide():
	assert calc.divide(10, 5) == 2
	assert calc.divide(-1, 1) == -1
	assert calc.divide(-6, -3) == 2
	assert calc.divide(5.0, 2) == 2.5

	# a better way using Context Manager
	with pytest.raises(ValueError):
		calc.divide(10, 0)