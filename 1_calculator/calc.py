#!/usr/bin/env python3

# pytest following tutorial: https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest


def add(x, y):
	if not isinstance(x, int) or not isinstance(y, int):
		raise TypeError('Can only process integer.')
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	if y == 0:
		raise ValueError('Can not divide by zero!')
	return x / y 