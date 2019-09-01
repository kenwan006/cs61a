'''Discussion 02'''

#Section I: More Environment Diagrams

'''Question 1.1'''
from operator import add
six = 1

def ty(one, a):
    fall = one(a, six)
    return fall
    
six = ty(add, 6)
fall = ty(add, 6)

'''Question 1.2'''
def curry2(h):
    def f(x):
        def g(y):
            return h(x, y)
        return g
    return f
    
make_adder = curry2(lambda x, y: x + y)
add_three = make_adder(3)
five = add_three(2)

'''Question 1.3'''
y = "y"
h = y
def y(y):
    h = "h"
    if y == h:
        return y + "i"
    y = lambda y: y(h)
    return lambda h: y(h)
    
y = y(y)(y)



#Section II: Recursion

'''Qustion 2.1 '''
def multiply(m, n):
	"""
	>>> multiply(5, 3)
	15
	"""
	if n == 1:
		return m

	return multiply(m, n-1) + m

'''Question 2.2'''
def countdown(n):
	"""
	>>> countdown(3)
	3
	2
	1
	"""
	if n == 0:
		return 
	print (n)
	countdown(n-1)

'''Qustion 2.3'''

def countup(n):
	"""
	>>> countup(3)
	1
	2
	3
	"""
	if n == 0:
		return 
	countup(n-1)
	print(n)

'''Question 2.4'''
def sum_digits(n):
	"""
	>>> sum_digits(7)
	7
	>>> sum_digits(30)
	3
	>>> sum_digits(228)
	12
	"""
	if n < 10:
		return n

	return sum_digits(n//10) + n % 10


#Section III: Tree Recursion. More than one recursive call is required.

'''Question 3.1'''
'''go up a fligth of staris that has n steps. either take 1 or 2 steps each time..'''
def count_stair_ways(n):
	if n == 0 or n == 1:
		return 1
	return count_stair_ways(n-1) + count_stair_ways(n-2)

'''Question 3.2'''
'''not take 1 or 2 steps but can take up to k steps each time'''
def count_k(n, k):
	"""
	>>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
	4
	>>> count_k(4, 4)
	8
	>>> count_k(10, 3)
	274
	>>> count_k(300, 1) # Only one step at a time
	1
	"""
	if n< 0:
		return 0
	if n == 0:
		return 1

	count = 0
	for i in range(1, k+ 1):
		count = count + count_k(n-i, k)

	return count






from doctest import testmod
testmod()






