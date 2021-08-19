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


def newton_raphson(expr, guess, tol, roots):
	"""
	Function to find the root of an expression using Newton-Raphson method.

	Parameters:
	expr:		input expression for which the root is calculated
	guess:		initial guess as input by the user
	tol:		maximum permissible error between the calculated root and the true root
	roots:		an array to store the calculated roots through the iterations to be plotted later
	"""

	differ = diffy(expr)
	diff_math = func(differ) 
	function = func(expr)

	x_new = guess - function(guess)/diff_math(guess)
	roots.append(x_new)

	if abs(x_new - guess) < tol:

		return roots

	else:

		return newton_raphson(expr, x_new, tol, roots)

def plot_func(expr, roots, guess):
	"""
	Function to plot the expression, the initial guess and all the calculated roots while highlighting the final correct root.

	Parameters:
	expr:		the expression to be plotted
	roots:		array of roots calculated by Newton-Raphson method
	guess:		initial guess input by the user
	"""

	function = func(expr)

	# Plotting the function by creating an array of Xs and Ys
	x = np.linspace(np.floor(roots[-1]-5), np.ceil(roots[-1]+5), 50)
	y = []

	for i in x:
		y.append(function(i))

	# An array of zeros the same length as the number of roots in arrays, so as to plot the roots
	roots_y = np.zeros(len(roots))

	fig = plt.figure(figsize=(8,7))

	ax1 = fig.add_axes([0.05, 0.05, 0.9, 0.9])

	ax1.plot(x, y, label="Function: %s"% expr)
	ax1.axhline(0, color='red', ls='--', alpha=0.5)
	ax1.scatter(roots[:-1], roots_y[:-1], color='black', s=10, alpha=0.8, edgecolor='black', label="Roots")
	ax1.scatter(guess, 0, color='red', s=15, label="Initial Guess: %s"% str(guess))
	ax1.scatter(roots[-1], 0, color="green", s=15, label="Final Root: %s"% str(round(roots[-1], 3)))

	ax1.set_title("Finding Roots: Newton Raphson Method")
	ax1.legend()

	plt.show()

# Sample input: 

# expr = "x - tan(x)"
# init_guess = 4.6
# error = 0.0001

points = []

expr = input("Enter a continuous function in x: ")
init_guess = float(input("Enter an initial guess for the root: "))
error = float(input("Enter the maximum permissible error of the root: "))

answers = newton_raphson(expr, init_guess, error, points)

plot_func(expr, answers, init_guess)

print(f"The root of {expr} by Newton-Raphson method: {round(answers[-1], 3)}")

