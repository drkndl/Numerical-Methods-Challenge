import numpy as np 
import matplotlib.pyplot as plt
import sympy as sp



def func(exp):
	"""
	Function to convert the expression to the Pythonic format to make mathematical calculations.

	Parameters:
	exp:	inputted expression by the user to be lambdified
	"""

	x = sp.symbols('x')
	return sp.utilities.lambdify(x, exp, "math")



def regula_falsi(exp, a, b, tol, points, count):
	"""
	Function to calculate the root of the expression through the bisection method.

	Parameters:
	exp:	inputted expression by the user whose root needs to be found
	a:		lower limit of the range
	b:		upper limit of the range
	tol:	maximum permissible error between the calculated root and the true solution
	points:	a list to save the roots calculated through the iterations
	count:	it ensures that checking for the permissible error of the root cannot be done in the first iteration which has only one root
	"""

	function = func(exp)


	# Checking to ensure the range given by the user is correct and a root to the expression lies between the range
	if function(a) * function(b) > 0:

		print(f"Invalid range of {a} and {b}. Ensure range is between a root by checking if both signs are different.")
		return  

	c = (a * function(b) - b * function(a))/(function(b) - function(a))
	points.append(c)

	if count > 1:

		if abs(points[-1] - points[-2]) < tol:

			return points 

	if function(a) * function(c) < 0:

		count += 1
		return regula_falsi(exp, a, c, tol, points, count)

	elif function(b) * function(c) < 0:

		count += 1
		return regula_falsi(exp, b, c, tol, points, count)



def plot_func(exp, array, a, b):
	"""
	A function to plot the expression and all the calculated roots, while highlighting the final correct root

	Parameters:
	exp:	inputted expression by the user which needs to be plotted
	a:		lower limit of the range
	b:		upper limit of the range
	array:	array of roots to be plotted
	"""

	function = func(exp)

	# Plotting the function by creating an array of Xs and Ys
	x = np.linspace(a, b, 20)
	y = []

	for i in x:
		y.append(function(i))

	# An array of zeros the same length as the number of roots in arrays, so as to plot the roots
	array_y = np.zeros(len(array))

	fig = plt.figure(figsize=(8,7))

	ax1 = fig.add_axes([0.05, 0.05, 0.9, 0.9])

	ax1.plot(x, y, label="Function: %s"% exp)
	ax1.axhline(0, color='red', ls='--', alpha=0.5)
	ax1.scatter(array[:-1], array_y[:-1], color='black', s=10, alpha=0.8, edgecolor='black', label="Roots")
	ax1.scatter(array[-1], 0, color="green", s=15, label="Final Root: %s"% str(round(array[-1], 3)))

	ax1.set_title("Finding Roots: Bisection Method")
	ax1.legend()

	plt.show()

roots = []
count = 1

expr = input("Enter a continuous function in x: ")
a, b = map(int, input("Enter the range with a space in between the two numbers: ").split())
error = float(input("Enter the max allowable tolerance: "))

# Example input values:

# expr = "x^3 - x - 2"
# a, b = 1, 2
# error = 0.001

final = regula_falsi(expr, a, b, error, roots, count)

plot_func(expr, final, a, b)

print("The root by regula falsi method: ", round(final[-1], 3))