import numpy as np 
import matplotlib.pyplot as plt 
import sympy as sp 


def func(exp):
	"""
	Function to convert the expression to the Pythonic format to make mathematical calculations.

	Parameters:
	exp:	input expression by the user to be lambdified
	"""

	x = sp.symbols('x')
	return sp.utilities.lambdify(x, exp, "math")


def diffy(exp):
	"""
	Function to find the differential of an expression.

	Parameters:
	exp:	input expression whose differential is calculated
	"""

	x = sp.symbols('x')
	return sp.diff(exp, x)

def newton_multivariate(exp, init):

	return "blah"

# def Jacobian(exp, init, jaco):

# 	for i in range()



jacobian = np.zeros((3,3))

a, b = 1, 2
print(f"Before: a = {a} and b = {b}")

b, a = a, b 
print(f"After: a = {a} and b = {b}")

a, b = b, a 
print(f"Swapping again: a = {a} and b = {b}")
