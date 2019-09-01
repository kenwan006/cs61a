'''Discussion 01'''  

#Section I Control : if statements/ boolean operators/ while loops

'''Quesion 1.1'''
#This should only take one line of code!
def wears_jacket(temp, raining):
	"""
	>>> wears_jacket(90, False)
	False
	>>> wears_jacket(40, False)
	True
	>>> wears_jacket(100, True)
	True
	"""
	return (temp < 60 or raining)


'''Question 1.2'''
def handle_overflow(s1, s2):
	"""
	>>> handle_overflow(27, 15)
	No overflow.
	>>> handle_overflow(35, 29)
	1 spot left in Section 2.
	>>> handle_overflow(20, 32)
	10 spots left in Section 1.
	>>> handle_overflow(35, 30)
	No space left in either section.
	"""
	if s1 < 30:
		if s2 >= 30:
			if s1 == 29:
				print('1 spot left in Section 1.')
			else:
				print('%s spots left in Section 1.' % (30 - s1))
		else:
			print('No overflow.')

	if s1 >= 30:
		if s2 >= 30:
			print('No space left in either section.')
		elif s2 == 29:
			print('1 spot left in Section 2.')
		else:
			print('%s spots left in Section 2.')


'''Question 1.3'''
def square(x):
	return x * x
def so_slow(num):
	x = num
	while x > 0:
		x = x + 1
	return x / 0
# calculate square(so_slow(5))  it's gonna be a dead loop

'''Question 1.4'''
def is_prime(n):
	if n == 1:
		return False
	i = 2
	while i < n:
		if n % i == 0:
			return False
		i += 1
	return True

#Section II Environment Diagrams



#Section III Higher Order Functions: function as arguments, functions as return values

'''Question 3.1'''
def keep_ints(cond, n):
	"""Print out all integers 1..i..n where cond(i) is true
	>>> def is_even(x):
		# Even numbers have remainder 0 when divided by 2
			return x % 2 == 0
	>>> keep_ints(is_even, 5)
	2
	4
	"""
	i = 1
	while i <= n:
		if cond(i):
			print (i)
		i += 1

'''Question 3.2'''
def outer(n):
	 def inner(m):
	 	return n - m
	 return inner
outer(61)
f = outer(10)
f(4)
outer(5)(4)	

'''Question 3.3 '''
def keep_ints(n):
	"""Returns a function which takes one parameter cond and
	prints out all integers 1..i..n where calling cond(i)
	returns True.
	>>> def is_even(x):
			return x % 2 == 0
	>>> keep_ints(5)(is_even)
	2
	4
	"""
	def g(cond):
		i = 1
		while i <= n:
			if cond(i):
				print(i)
			i += 1

	return g


#test
from doctest import testmod
testmod()