'''Discusstion 04'''

#Question 2.3 write a function that updates and prints a value x based on input functions
def memory(n):
	"""
	>>> f = memory(10)
	>>> f = f(lambda x: x * 2)
	20
	>>> f = f(lambda x: x - 7)
	13
	>>> f = f(lambda x: x > 5)
	True
	"""
	def foo(fn):
		nonlocal n
		n = fn(n)
		print (n)
		return foo

	return foo

#Question 3.2 
def add_this_many(x, el, lst):
	""" Adds el to the end of lst the number of times x occurs
	in lst.
	>>> lst = [1, 2, 4, 2, 1]
	>>> add_this_many(2, 5, lst)
	>>> lst
	[1, 2, 4, 2, 1, 5, 5]
	>>> add_this_many(2, 2, lst)
	>>> lst
	[1, 2, 4, 2, 1, 5, 5, 2, 2]
	"""
	while x > 0:
		lst.append(el)
		x -= 1

	return

#Question 3.3
def reverse(lst):
	""" Reverses lst in place.
	>>> x = [3, 2, 4, 5, 1]
	>>> reverse(x)
	>>> x
	[1, 5, 4, 2, 3]
	"""
	i = 0
	while i < len(lst) // 2:
		lst[i], lst[len(lst) -1 -i] = lst[len(lst) -1 -i], lst[i]
		i += 1


